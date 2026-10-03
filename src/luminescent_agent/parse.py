"""把 Crossref 的原始 JSON 条目转换成 Paper 对象。

单独成文件的原因：以后换数据源（PubMed / 自建实验数据库）时，
只改 fetch 层和这个文件，其他代码不动。
"""
from typing import Any
from .models import Paper
def _first_text(value: Any) -> str | None:
    """Crossref 的 title / container-title 有时是数组，有时是字符串，有时缺失。

    统一收口成一个函数，避免在 parse_item 里到处写 if isinstance(...)。
    """
    if isinstance(value, list):
        if not value:
            return None
        text = str(value[0]).strip()
        return text or None
    if isinstance(value, str):
        text = value.strip()
        return text or None
    return None

def _extract_year(item:dict) -> int | None:

    published =item.get("published") or item.get("published-print") or {}
    data_parts=published.get("data-parts") or []
    if not data_parts or not data_parts[0]:
        return None
    year = data_parts[0][0]
    return int(year) if isinstance(year,int) else None

def _extract_frist_author(item:dict) -> str | None:
    author = item.get("author") or []
    if not author:
        return None
    first=author[0]
    family =str(first.get("family") or "").strip()
    given=str(first.get("given") or "").strip()
    full =f"{family} {given}".strip()
    return full or None

def parse_item(item:dict) -> Paper:
    return Paper(
        doi=str(item.get("DOI") or "").strip(),
        title=_first_text(item.get("title") or "无标题"),
        journal=_first_text(item.get("container-title")),
        year=_extract_year(item),
        first_author =_extract_frist_author(item),
    )