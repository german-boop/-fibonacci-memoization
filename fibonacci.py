def fibonacci(n, memo={}):
    """Calculate nth Fibonacci number using memoization"""
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(f"Fibonacci(200): {fibonacci(200)}")
print(f"Fibonacci(301): {fibonacci(301)}")
