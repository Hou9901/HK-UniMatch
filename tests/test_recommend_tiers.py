"""Unit tests for match_system.recommend() tier inclusion (no HTTP layer)."""

from __future__ import annotations

from match_system import recommend


class TestTierRecommendationLogic:
    def test_strong_t1_university_lists_all_three_hk_tiers(self):
        """武汉大学 (T1) with solid GPA/IELTS should pass both hot and cold for each HK group."""
        out = recommend("武汉大学", 3.5, 6.5, "business")
        tiers = [x["港校梯队"] for x in out["推荐列表"]]
        assert len(tiers) == 3
        assert tiers[0] == "港大/港中文/港科大"
        assert "Top5+城大理工" in tiers
        assert "全港八大" in tiers

    def test_unknown_university_weak_scores_empty_recommendation_list(self):
        """T3 bars + low scores: hot and/or cold fail so no tier should be listed."""
        out = recommend("Unknown College XYZ", 2.0, 5.0, "business")
        assert out["自动判定等级"] == "T3"
        assert out["推荐列表"] == []

    def test_top3_tier_omitted_when_hot_fails_even_if_cold_passes(self):
        """T2 profile: cold clears Top3 bar but hot does not — tier must not be listed."""
        out = recommend("深圳大学", 3.5, 6.5, "business")
        labels = {x["港校梯队"] for x in out["推荐列表"]}
        assert "港大/港中文/港科大" not in labels

    def test_any_listed_tier_has_no_failed_hot_status(self):
        for item in recommend("武汉大学", 3.5, 6.5, "business")["推荐列表"]:
            assert "❌" not in item["热门专业"]["状态"], item
