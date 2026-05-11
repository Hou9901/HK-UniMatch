from __future__ import annotations

from flask import Flask, request, jsonify, send_from_directory
import csv
import logging
import os
from typing import Optional

from match_system import MAJOR_CONFIG, recommend

app = Flask(__name__, static_url_path='')

logger = logging.getLogger(__name__)


def toefl_to_ielts_equivalent(toefl_total: float) -> float:
    """Map TOEFL iBT total score (0–120) to an approximate IELTS band (simple table)."""
    t = float(toefl_total)
    if t >= 118:
        return 9.0
    if t >= 115:
        return 8.5
    if t >= 110:
        return 8.0
    if t >= 102:
        return 7.5
    if t >= 94:
        return 7.0
    if t >= 79:
        return 6.5
    if t >= 60:
        return 6.0
    if t >= 46:
        return 5.5
    if t >= 35:
        return 5.0
    if t >= 32:
        return 4.5
    return 4.0


def score_to_ielts_for_filter(exam_type: str, score: float) -> float:
    et = exam_type.strip().upper()
    if et == "TOEFL":
        return toefl_to_ielts_equivalent(score)
    if et == "IELTS":
        return float(score)
    raise ValueError(f"Unsupported exam_type: {exam_type!r}")


def row_english_requirement_as_ielts_band(row: dict) -> Optional[float]:
    """
    CSV English requirement as an IELTS-comparable band for filtering.
    Prefer a numeric IELTS cell; otherwise use TOEFL (total score) mapped via toefl_to_ielts_equivalent.
    """
    raw_ielts = row.get("IELTS", "")
    cell_i = "" if raw_ielts is None else str(raw_ielts).strip()
    if cell_i:
        try:
            return float(cell_i)
        except (ValueError, TypeError):
            pass

    raw_toefl = row.get("TOEFL", "")
    cell_t = "" if raw_toefl is None else str(raw_toefl).strip()
    if cell_t:
        try:
            return toefl_to_ielts_equivalent(float(cell_t))
        except (ValueError, TypeError):
            pass

    return None


UNI_SHORT_TO_FULL = {
    "HKU": "The University of Hong Kong",
    "CUHK": "The Chinese University of Hong Kong",
    "HKUST": "The Hong Kong University of Science and Technology",
    "PolyU": "The Hong Kong Polytechnic University",
    "CityU": "City University of Hong Kong",
    "HKBU": "Hong Kong Baptist University",
    "LingnanU": "Lingnan University",
    "EdUHK": "The Education University of Hong Kong"
}

ALL_SHORTS = list(UNI_SHORT_TO_FULL.keys())

TIER_DISPLAY_TO_SHORTS = {
    "港大/港中文/港科大": ["HKU", "CUHK", "HKUST"],
    "Top5+城大理工": ["CityU", "PolyU"],
    "全港八大": ["HKBU", "LingnanU", "EdUHK"]
}

MAJOR_TYPE_TO_CATEGORY = {
    "business": "Business",
    "stem": "Engineering&Technology",
    "social": "Social Sciences",
    "arts": "Humanities",
    "media": "Humanities"
}

ALLOWED_MAJOR_TYPES = frozenset(MAJOR_CONFIG.keys())

# Programme category display order (matches UI labels); unknown / missing sort last ("Other").
PROGRAMME_CATEGORY_ORDER = (
    "Business",
    "Engineering&Technology",
    "Social Sciences",
    "Humanities",
    "Art",
    "Medicine&Health",
    "Education",
)


def _category_sort_rank(category: Optional[str]) -> int:
    if category is None or not str(category).strip():
        return len(PROGRAMME_CATEGORY_ORDER)
    key = str(category).strip()
    try:
        return PROGRAMME_CATEGORY_ORDER.index(key)
    except ValueError:
        return len(PROGRAMME_CATEGORY_ORDER)


def sort_programmes_for_display(programmes: list[dict]) -> list[dict]:
    """
    Sort programmes: keep each university block in first-seen order, do not reorder universities.
    Within each university: category order, then university name, then programme name (case-insensitive).
    """
    if not programmes:
        return programmes
    uni_seq: list[str] = []
    seen: set[str] = set()
    for p in programmes:
        u = p.get("University") or ""
        if u not in seen:
            seen.add(u)
            uni_seq.append(u)
    rank_of = {u: i for i, u in enumerate(uni_seq)}
    fallback = len(uni_seq)

    def sort_key(p: dict) -> tuple[int, int, str, str]:
        u = p.get("University") or ""
        prog = p.get("Programme") or ""
        return (
            rank_of.get(u, fallback),
            _category_sort_rank(p.get("Category")),
            str(u).casefold(),
            str(prog).casefold(),
        )

    return sorted(programmes, key=sort_key)


CSV_PATH = os.path.join(os.path.dirname(__file__), "Mastersportal.csv")

@app.route("/")
def index():
    return send_from_directory(os.path.dirname(__file__), "merged_home_page.html")

@app.route("/api/match", methods=["POST"])
def api_match():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    university = data.get("university")
    gpa = data.get("gpa")
    major_type = data.get("major_type")
    exam_type = data.get("exam_type")
    score = data.get("score")
    # Legacy: { "ielts": 6.5 } treated as IELTS
    if score is None and data.get("ielts") is not None:
        exam_type = exam_type or "IELTS"
        score = data.get("ielts")
    if not all([university, gpa, major_type is not None, exam_type, score is not None]):
        return jsonify({
            "error": "Missing required fields: university, gpa, major_type, exam_type, score"
        }), 400
    if major_type not in ALLOWED_MAJOR_TYPES:
        return jsonify({"error": f"Invalid major_type: {major_type!r}"}), 400
    try:
        gpa = float(gpa)
        score = float(score)
    except (ValueError, TypeError):
        return jsonify({"error": "gpa and score must be numeric"}), 400
    if not isinstance(exam_type, str) or not exam_type.strip():
        return jsonify({"error": "exam_type must be a non-empty string"}), 400
    try:
        ielts = score_to_ielts_for_filter(exam_type, score)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    result = recommend(university, gpa, ielts, major_type)

    category = MAJOR_TYPE_TO_CATEGORY.get(major_type, "Business")
    csv_rows = []
    try:
        with open(CSV_PATH, encoding="latin1") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Category"] == category:
                    csv_rows.append(row)
    except FileNotFoundError:
        pass

    for item in result["推荐列表"]:
        shorts = TIER_DISPLAY_TO_SHORTS.get(item["港校梯队"])
        if shorts:
            full_names = {UNI_SHORT_TO_FULL[s] for s in shorts if s in UNI_SHORT_TO_FULL}
            hot_status = item["热门专业"]["状态"]
            if "✅" in hot_status:
                match_level = "✅ 有竞争力"
            elif "⚠️" in hot_status:
                match_level = "⚠️ 有风险"
            else:
                match_level = hot_status
            programmes = []
            for r in csv_rows:
                if r["University"] not in full_names:
                    continue
                req_band = row_english_requirement_as_ielts_band(r)
                if req_band is None:
                    logger.warning(
                        "Skipping programme row: empty or non-numeric IELTS and TOEFL "
                        "(programme=%r, university=%r, raw_ielts=%r, raw_toefl=%r)",
                        r.get("Programme"),
                        r.get("University"),
                        r.get("IELTS"),
                        r.get("TOEFL"),
                    )
                    continue
                if req_band <= ielts:
                    programmes.append({
                        "Programme": r["Programme"],
                        "University": r["University"],
                        "Category": r["Category"],
                        "IELTS": r["IELTS"],
                        "Duration": r["Duration"],
                        "Apply date": r["Apply date"],
                        "match_level": match_level
                    })
            item["programmes"] = sort_programmes_for_display(programmes)
        else:
            item["programmes"] = []

    return jsonify(result)

@app.route("/api/programs", methods=["GET"])
def api_programs():
    uni_short = request.args.get("university")
    full_name = UNI_SHORT_TO_FULL.get(uni_short) if uni_short else None
    results = []
    try:
        with open(CSV_PATH, encoding="latin1") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if full_name is None or row["University"] == full_name:
                    results.append({
                        "University": row["University"],
                        "Programme": row["Programme"],
                        "Category": row["Category"],
                        "IELTS": row["IELTS"],
                        "Duration": row["Duration"],
                        "Apply date": row["Apply date"]
                    })
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500
    return jsonify(sort_programmes_for_display(results))

if __name__ == "__main__":
    flask_env = os.environ.get("FLASK_ENV", "production").strip().lower()
    in_development = flask_env == "development"

    # Never enable the interactive debugger outside development, even if FLASK_DEBUG is set.
    debug_env = os.environ.get("FLASK_DEBUG", "true" if in_development else "false").strip().lower()
    debug_on = in_development and debug_env in ("1", "true", "yes", "on")

    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", "5000"))

    app.run(debug=debug_on, host=host, port=port)
