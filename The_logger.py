from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("--- 开始执行 ---")
        result = func(*args, **kwargs)
        print("--- 结束执行 ---")
        print(func.__name__)
        return result
    return wrapper
    
@logger
def add(x, y):
    return x + y

print(add(1, 2))