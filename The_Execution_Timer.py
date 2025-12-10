import time

class Timer:
    
    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed = self.end_time - self.start_time
        print(f"代码运行耗时: {self.elapsed} s")
        
with Timer():
    result = sum(range(100000000))