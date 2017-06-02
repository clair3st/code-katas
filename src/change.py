"""Change calculator."""


def change(n):
    """Given input number return min amound of coins required."""
    min_coins = n
    if n in [1, 3, 5]:
        return 1
    else:
        for i in [c for c in [1, 3, 5] if c <= n]:
            coin = 1 + change(n - i)
            if coin < min_coins:
                min_coins = coin
    return min_coins
