def fibonacci(n):
    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_series[i - 1] + fibonacci_series[i - 2]
        fibonacci_series.append(next_number)
    return fibonacci_series



n = 10
fib_series = fibonacci(n)
print("Fibonacci series up to", n, "terms:", fib_series)
