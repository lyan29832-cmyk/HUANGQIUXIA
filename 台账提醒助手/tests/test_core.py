from __future__ import annotations

from datetime import date, datetime, timedelta
from pathlib import Path

import pytest

from core import (
    AppConfig,
    LedgerRow,
    check_and_notify,
    create_template,
    find_new_direct_impacts,
    infer_smtp,
    read_ledger_rows,
)


def _row(**kwargs: object) -> LedgerRow:
    data = {
        "row_key": "001",
        "item_id": "001",
        "title": "事项A",
        "impact": "间接影响",
        "owner": "张三",
        "email": "a@example.com",
        "wecom": "zhangsan",
        "row_number": 2,
    }
    data.update(kwargs)
    return LedgerRow(**data)  # type: ignore[arg-type]


def test_find_new_direct_impacts_detects_change() -> None:
    old = {"001": {"impact": "间接影响"}}
    rows = [_row(impact="直接影响")]
    hits = find_new_direct_impacts(old, rows)
    assert len(hits) == 1
    assert hits[0].item_id == "001"


def test_find_new_direct_impacts_ignores_existing() -> None:
    old = {"001": {"impact": "直接影响"}}
    rows = [_row(impact="直接影响")]
    assert find_new_direct_impacts(old, rows) == []


def test_find_new_direct_impacts_detects_new_row() -> None:
    hits = find_new_direct_impacts({}, [_row(impact="直接影响")])
    assert len(hits) == 1


def test_infer_smtp_preset() -> None:
    assert infer_smtp("a@qq.com", "QQ邮箱") == ("smtp.qq.com", 465)
    assert infer_smtp("a@outlook.com", "Outlook / 微软") == ("smtp.office365.com", 587)


def test_create_and_read_template(tmp_path: Path) -> None:
    path = create_template(tmp_path / "台账.xlsx")
    rows, missing, sheet = read_ledger_rows(path)
    assert missing == []
    assert sheet == "台账"
    assert [row.item_id for row in rows] == ["001", "002"]


def test_check_first_run_does_not_notify(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    excel = create_template(tmp_path / "台账.xlsx")
    sent: list[str] = []
    monkeypatch.setattr("core.notify_hits", lambda cfg, hits: sent.append("sent") or (0, []))
    cfg = AppConfig(excel_path=str(excel), enable_email=False, enable_wecom=False)
    result = check_and_notify(tmp_path, cfg, ignore_mtime=True)
    assert result.first_run is True
    assert result.hits == []
    assert sent == []


def test_check_notifies_new_direct_impact(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    excel = create_template(tmp_path / "台账.xlsx")
    cfg = AppConfig(excel_path=str(excel), enable_email=False, enable_wecom=False)
    check_and_notify(tmp_path, cfg, ignore_mtime=True)

    from openpyxl import load_workbook

    wb = load_workbook(excel)
    wb.active["C2"] = "直接影响"
    wb.save(excel)
    wb.close()

    captured: list[str] = []

    def fake_notify(config: AppConfig, hits: list[LedgerRow]) -> tuple[int, list[str]]:
        captured.extend(h.item_id for h in hits)
        return len(hits), []

    monkeypatch.setattr("core.notify_hits", fake_notify)
    result = check_and_notify(tmp_path, cfg, ignore_mtime=True)
    assert captured == ["001"]
    assert result.notified == 1


def test_skip_when_file_not_updated_today(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    excel = create_template(tmp_path / "台账.xlsx")
    cfg = AppConfig(excel_path=str(excel))
    check_and_notify(tmp_path, cfg, ignore_mtime=True)

    old = datetime.now() - timedelta(days=2)
    import os

    ts = old.timestamp()
    os.utime(excel, (ts, ts))

    sent: list[str] = []
    monkeypatch.setattr("core.notify_hits", lambda cfg, hits: sent.append("sent") or (1, []))
    result = check_and_notify(tmp_path, cfg, ignore_mtime=False, today=date.today())
    assert result.not_updated_today is True
    assert sent == []
