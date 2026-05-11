"""HTTP tests for POST /api/match: validation, CSV handling, IELTS/TOEFL filtering."""

from __future__ import annotations


class TestMajorTypeValidation:
    def test_invalid_major_type_returns_400(self, client, match_payload_base):
        payload = {**match_payload_base, "major_type": "law"}
        res = client.post("/api/match", json=payload)
        assert res.status_code == 400
        body = res.get_json()
        assert "error" in body
        assert "Invalid major_type" in body["error"]
        assert "law" in body["error"]

    def test_valid_major_types_return_200(self, client, match_payload_base):
        for mt in ("business", "stem", "social", "arts", "media"):
            payload = {**match_payload_base, "major_type": mt}
            res = client.post("/api/match", json=payload)
            assert res.status_code == 200, (mt, res.get_data(as_text=True))
            data = res.get_json()
            assert "推荐列表" in data
            assert isinstance(data["推荐列表"], list)

    def test_missing_major_type_returns_400(self, client):
        res = client.post(
            "/api/match",
            json={
                "university": "武汉大学",
                "gpa": 3.5,
                "exam_type": "IELTS",
                "score": 6.5,
            },
        )
        assert res.status_code == 400


class TestCsvParsing:
    def test_non_numeric_ielts_row_not_in_programmes(self, client, match_payload_base):
        """Row with '6.0 or 6.5' must not crash and must not appear as a programme."""
        res = client.post("/api/match", json=match_payload_base)
        assert res.status_code == 200
        data = res.get_json()
        names = _all_programme_names(data)
        assert "Weird IELTS" not in names

    def test_empty_ielts_row_not_in_programmes(self, client, match_payload_base):
        res = client.post("/api/match", json=match_payload_base)
        assert res.status_code == 200
        names = _all_programme_names(res.get_json())
        assert "Empty IELTS" not in names

    def test_toefl_only_row_uses_toefl_column_when_ielts_empty(self, client, match_payload_base):
        """TOEFL 79 -> IELTS 6.5 equivalent; user IELTS 6.5 should include the programme."""
        res = client.post("/api/match", json=match_payload_base)
        assert res.status_code == 200
        top = _tier_programmes(res.get_json(), "港大/港中文/港科大")
        names = {p["Programme"] for p in top}
        assert "TOEFL Only Biz" in names


class TestIeltsToeflScoreFiltering:
    def test_ielts_band_filters_programmes_by_requirement(self, client, match_payload_base):
        """User IELTS 6.5: include req 6.0, exclude req 7.0 for same tier/university set."""
        res = client.post("/api/match", json=match_payload_base)
        assert res.status_code == 200
        data = res.get_json()
        top = _tier_programmes(data, "港大/港中文/港科大")
        names = {p["Programme"] for p in top}
        assert "Req Six" in names
        assert "Req Seven" not in names

    def test_toefl_converted_to_ielts_for_filtering(self, client, match_payload_base):
        """TOEFL 94 maps to IELTS 7.0 equivalent — include programme requiring 7.0."""
        payload = {**match_payload_base, "exam_type": "TOEFL", "score": 94}
        res = client.post("/api/match", json=payload)
        assert res.status_code == 200
        top = _tier_programmes(res.get_json(), "港大/港中文/港科大")
        names = {p["Programme"] for p in top}
        assert "Req Seven" in names
        assert "Req Six" in names

    def test_toefl_lower_band_excludes_high_requirement(self, client, match_payload_base):
        """TOEFL 79 maps to IELTS 6.5 — exclude programme requiring 7.0."""
        payload = {**match_payload_base, "exam_type": "TOEFL", "score": 79}
        res = client.post("/api/match", json=payload)
        assert res.status_code == 200
        top = _tier_programmes(res.get_json(), "港大/港中文/港科大")
        names = {p["Programme"] for p in top}
        assert "Req Seven" not in names
        assert "Req Six" in names

    def test_legacy_ielts_field_still_works(self, client, match_payload_base):
        payload = {
            "university": match_payload_base["university"],
            "gpa": match_payload_base["gpa"],
            "major_type": match_payload_base["major_type"],
            "ielts": 6.5,
        }
        res = client.post("/api/match", json=payload)
        assert res.status_code == 200
        top = _tier_programmes(res.get_json(), "港大/港中文/港科大")
        assert any(p["Programme"] == "Req Six" for p in top)


class TestTierRecommendationViaApi:
    def test_response_includes_expected_tier_labels(self, client, match_payload_base):
        res = client.post("/api/match", json=match_payload_base)
        assert res.status_code == 200
        data = res.get_json()
        tiers = [item["港校梯队"] for item in data["推荐列表"]]
        assert tiers == [
            "港大/港中文/港科大",
            "Top5+城大理工",
            "全港八大",
        ]
        for item in data["推荐列表"]:
            assert "热门专业" in item and "冷门保底" in item
            assert "状态" in item["热门专业"]

    def test_cityu_row_appears_in_top5_tier_only(self, client, match_payload_base):
        res = client.post("/api/match", json=match_payload_base)
        data = res.get_json()
        top3_names = {p["Programme"] for p in _tier_programmes(data, "港大/港中文/港科大")}
        top5_names = {p["Programme"] for p in _tier_programmes(data, "Top5+城大理工")}
        assert "City Six" not in top3_names
        assert "City Six" in top5_names


def _tier_programmes(data: dict, tier_label: str) -> list:
    for item in data["推荐列表"]:
        if item["港校梯队"] == tier_label:
            return item.get("programmes") or []
    raise AssertionError(f"Tier not found: {tier_label!r}")


def _all_programme_names(data: dict) -> set[str]:
    out: set[str] = set()
    for item in data["推荐列表"]:
        for p in item.get("programmes") or []:
            out.add(p["Programme"])
    return out
