def fib_gen(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

        
for i in fib_gen(100):
    print(i)