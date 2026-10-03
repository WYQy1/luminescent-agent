import  json
from pathlib import Path
from luminescent_agent.parse import parse_item
FIXTURE = Path(__file__).parent / "fixtures" / "crossref_sample.json"

def load_items() -> list[dict]:
    raw=json.loads(FIXTURE.read_text(encoding='utf-8'))
    return raw["message"]["items"]

def test_fixture_reads_and_has_two_items():
    items=load_items()
    assert len(items)==2
    assert  items[0]["DOI"]== "10.1016/j.jlumin.2021.118000"

def test_first_paper_fields():
    paper =parse_item(load_items()[0])
    assert paper.year==2021
    assert paper.journal =="Journal of Luminescence"
    assert paper.first_author =="Zhang Wei"
    assert "Eu3+" in paper.title

def test_missing_journal_and_author_does_not_crash():
    paper =parse_item(load_items()[1])
    assert paper.journal is None
    assert paper.first_author is None
    assert paper.year is None
    assert paper.title =="Thermoluminescence study of LiF:Mg,Ti"

def test_empty_item_does_not_crash():
    paper =parse_item({})
    assert paper.doi==""
    assert paper.title=="无标题"
    assert paper.journal is None
    assert paper.year is None
    assert paper.first_author is None