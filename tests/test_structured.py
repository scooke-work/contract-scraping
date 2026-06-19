"""Offline unit tests for the structured-extraction post-pass (no network)."""
import pytest

import extract_structured as es


SAMPLE = """
MASTER SERVICES AGREEMENT
This Master Services Agreement is entered into as of January 5, 2020 by and between
Acme Corporation and Beta LLC. This Agreement shall be governed by the laws of the
State of Delaware. Net 30 payment terms apply. Each party shall indemnify the other.
The parties shall keep all information confidential. This Agreement will automatically
renew for successive one-year terms. In no event shall either party's aggregate
liability exceed the fees paid in the prior twelve months. Force majeure events
excuse performance. Either party may assign this Agreement only with consent.
"""


def test_heuristic_extract_core_fields():
    f = es.heuristic_extract(SAMPLE)
    assert f["governing_law"].lower().startswith("delaware")
    assert f["indemnification"] is True
    assert f["confidentiality"] is True
    assert f["payment_terms"] == "Net 30"
    assert f["effective_date"]                      # "January 5, 2020"
    for clause in ("indemnification", "limitation of liability", "force majeure",
                   "auto-renewal", "confidentiality"):
        assert clause in f["clause_inventory"]


def test_heuristic_extract_parties_best_effort():
    f = es.heuristic_extract(SAMPLE)
    assert any("Acme" in p for p in f["parties"])


def test_heuristic_shape_matches_empty_fields():
    f = es.heuristic_extract("nothing useful here")
    assert set(f) == set(es.EMPTY_FIELDS)


def test_make_client_without_key(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    with pytest.raises(es.LLMUnavailable):
        es.make_client()


def test_llm_extract_parses_tool_use_and_fills_empties():
    class Block:
        type = "tool_use"
        input = {"agreement_type": "MSA", "parties": ["A", "B"],
                 "governing_law": "New York",
                 "clause_inventory": ["indemnification"], "summary": "x"}

    class Resp:
        content = [Block()]

    class FakeClient:
        class messages:                       # noqa: N801 - mimic SDK shape
            @staticmethod
            def create(**_kw):
                return Resp()

    out = es.llm_extract(FakeClient(), "claude-sonnet-4-6", "contract text", 1000)
    assert out["agreement_type"] == "MSA"
    assert out["parties"] == ["A", "B"]
    assert out["payment_terms"] == ""         # missing key filled from EMPTY_FIELDS
