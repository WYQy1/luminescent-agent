"""基础装饰器练习：接收并传递任意位置参数和关键字参数。"""
from functools import wraps


def check(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)
    return inner


@check
def login(*args, **kwargs):
    print(args, kwargs)


if __name__ == "__main__":
    login(1, 2, c=18)
