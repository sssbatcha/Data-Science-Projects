def fib(n):
    fib_series = [0,1]
    while len(fib_series)< n:
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series[:n]
n = int(input("Enter a num:"))
result = fib(n)
print(f"The first {n} numbers in the Fibonacci series are:{result}")
