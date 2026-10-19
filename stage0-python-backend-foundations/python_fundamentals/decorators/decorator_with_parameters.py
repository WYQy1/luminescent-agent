"""带参数的装饰器练习：根据运算符输出提示，再执行原函数。"""
from functools import wraps


def logging(op):
    def decorator(fn):
        @wraps(fn)
        def inner(num1, num2):
            if op == "+":
                print("进行加法运算")
            elif op == "-":
                print("进行减法运算")
            else:
                raise ValueError(f"暂不支持的运算符：{op}")
            return fn(num1, num2)
        return inner
    return decorator


@logging("+")
def add(a, b):
    return a + b


@logging("-")
def sub(a, b):
    return a - b


if __name__ == "__main__":
    print(add(1, 2))
    print(sub(1, 3))
