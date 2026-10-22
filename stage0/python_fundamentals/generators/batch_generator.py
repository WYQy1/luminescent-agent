"""将可切片序列按 batch_size 分批生成。"""


def batch_generator(data, batch_size):
    if batch_size <= 0:
        raise ValueError("batch_size 必须大于 0")
    for start in range(0, len(data), batch_size):
        yield data[start:start + batch_size]


if __name__ == "__main__":
    for batch in batch_generator(list(range(1, 11)), 3):
        print(batch)
