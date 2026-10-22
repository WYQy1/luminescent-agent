"""计时装饰器练习。"""
import time
from functools import wraps


def timer(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"执行时间为 {elapsed:.6f} 秒")
        return result
    return inner


@timer
def sample_task():
    time.sleep(1)
    return "任务完成"


if __name__ == "__main__":
    print(sample_task())
