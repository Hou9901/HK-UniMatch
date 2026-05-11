"""Shared fixtures: project root on path, Flask client, minimal CSV for /api/match."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


@pytest.fixture
def minimal_csv(tmp_path: Path) -> Path:
    """Tiny CSV with controlled IELTS cells for filtering / parsing tests."""
    p = tmp_path / "programs.csv"
    p.write_text(
        "University,Programme,Category,IELTS,Duration,Apply date,TOEFL\n"
        "The University of Hong Kong,Req Six,Business,6.0,1 year,01-Jan,\n"
        "The University of Hong Kong,Req Seven,Business,7.0,1 year,01-Jan,\n"
        "The University of Hong Kong,Weird IELTS,Business,6.0 or 6.5,1 year,01-Jan,\n"
        "The University of Hong Kong,Empty IELTS,Business,,1 year,01-Jan,\n"
        "The University of Hong Kong,TOEFL Only Biz,Business,,1 year,01-Jan,79\n"
        "City University of Hong Kong,City Six,Business,6.0,1 year,01-Jan,\n",
        encoding="utf-8",
    )
    return p


@pytest.fixture
def app_module(minimal_csv, monkeypatch):
    import app as app_module

    monkeypatch.setattr(app_module, "CSV_PATH", str(minimal_csv))
    app_module.app.config.update(TESTING=True)
    return app_module


@pytest.fixture
def client(app_module):
    return app_module.app.test_client()


@pytest.fixture
def match_payload_base():
    """Profile that yields three HK tiers under current recommend() rules (business)."""
    return {
        "university": "武汉大学",
        "gpa": 3.5,
        "major_type": "business",
        "exam_type": "IELTS",
        "score": 6.5,
    }
