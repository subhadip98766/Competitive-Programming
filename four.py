def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, a + b
    return b


# Example test
print(climbStairs(2))  # 2
print(climbStairs(3))  # 3
