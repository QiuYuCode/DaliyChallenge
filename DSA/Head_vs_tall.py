from functools import wraps
import time

def time_count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)        
        end_time = time.time()
        print(f"use time: {end_time - start_time}")
        return result
    return wrapper

@time_count
def test_append():
    empty_list = []
    for i in range(50000):
        empty_list.append(i)
        

@time_count
def test_insert():
    empty_list = []
    for i in range(50000):
        empty_list.insert(0, i)

test_append()

test_insert()