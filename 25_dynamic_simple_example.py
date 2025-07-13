def fib(n):
    memo = [0] * (n + 1)  # 🧠 A place to remember things

    if n == 0:
        return 0
    if n == 1:
        return 1

    memo[0] = 0  # Fib(0)
    memo[1] = 1  # Fib(1)

    for i in range(2, n + 1):  # 🧱 Build answers from bottom up
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]
