from dataclasses import dataclass
@dataclass
class Paper:
    doi: str
    title: str
    journal: str |None
    year: str | None
    first_author: str | None
