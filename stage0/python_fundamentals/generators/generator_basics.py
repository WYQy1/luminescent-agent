"""生成器表达式与 yield 生成器的基础练习。"""


def number_generator(n):
    """依次生成 0 到 n-1。"""
    for i in range(n):
        yield i


if __name__ == "__main__":
    data = (x for x in range(5))
    print(next(data))
    print(next(data))
    for item in data:
        print(item)

    for item in number_generator(5):
        print(item)
