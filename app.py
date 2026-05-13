from __future__ import annotations

from flask import Flask, request, jsonify, send_from_directory
import csv
import logging
import os
from typing import Optional

from match_system import (
    ALL_UNIVERSITIES, MAJOR_CONFIG, recommend,
    toefl_to_ielts_equivalent, score_to_ielts_for_filter, row_english_requirement_as_ielts_band,
    UNI_SHORT_TO_FULL, ALL_SHORTS, TIER_DISPLAY_TO_SHORTS, MAJOR_TYPE_TO_CATEGORY,
    ALLOWED_MAJOR_TYPES, PROGRAMME_CATEGORY_ORDER, sort_programmes_for_display,
    enrich_recommendations_with_programmes, get_programmes_from_csv
)

app = Flask(__name__, static_url_path='')

logger = logging.getLogger(__name__)


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
    if university not in ALL_UNIVERSITIES:
        logger.warning("Invalid university input: %r", university)
        return jsonify({"error": f"未收录该本科院校: '{university}'"}), 400
    result = recommend(university, gpa, ielts, major_type)

    result = enrich_recommendations_with_programmes(result, ielts, major_type, CSV_PATH, logger)

    return jsonify(result)

@app.route("/api/programs", methods=["GET"])
def api_programs():
    uni_short = request.args.get("university")
    results = get_programmes_from_csv(CSV_PATH, uni_short)
    return jsonify(results)

if __name__ == "__main__":
    flask_env = os.environ.get("FLASK_ENV", "production").strip().lower()
    in_development = flask_env == "development"

    # Never enable the interactive debugger outside development, even if FLASK_DEBUG is set.
    debug_env = os.environ.get("FLASK_DEBUG", "true" if in_development else "false").strip().lower()
    debug_on = in_development and debug_env in ("1", "true", "yes", "on")

    host = os.environ.get("FLASK_RUN_HOST", "127.0.0.1")
    port = int(os.environ.get("FLASK_RUN_PORT", "5000"))

    app.run(debug=debug_on, host=host, port=port)
