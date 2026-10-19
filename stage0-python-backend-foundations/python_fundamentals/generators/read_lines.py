"""使用生成器逐行读取文本。"""
from pathlib import Path
from typing import Iterator


def read_lines(file_path: str | Path) -> Iterator[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")


if __name__ == "__main__":
    data_file = Path(__file__).parent / "data" / "sample.txt"
    for line in read_lines(data_file):
        print(line)
