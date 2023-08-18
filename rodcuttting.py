def rod_cutting(lengths, prices, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_price = 0
        for j in range(1, i + 1):
            max_price = max(max_price, prices[j - 1] + dp[i - j])
        dp[i] = max_price

    return dp[n]

# Example input
rod_lengths = [1, 2, 3, 4, 5, 6, 7, 8]
rod_prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 4

max_value = rod_cutting(rod_lengths, rod_prices, rod_length)
print(f"The maximum value that can be obtained is: {max_value}")
