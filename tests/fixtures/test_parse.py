import  json
from pathlib import Path
FIXTURES = Path(__file__).parent / 'fixtures'

def load_items() -> list[dict]:
    raw=json.load(FIXTURES.read_text(encoding='utf-8'))
    return raw["message"]["items"]

def test_fixtre_reads_and_has_one_items():
    items=load_items()
    assert len(items)==1
    assert  items[0]["DOI"]== "10.1016/j.jlumin.2021.118000"

