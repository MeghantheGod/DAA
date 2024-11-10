def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# User input
n = int(input("Enter the number of items: "))
values = input("Enter the value of the item{} in order:".format(n)).split()
values = [int(v) for v in values]
weights = input("Enter the weight of the item{} in order:".format(n)).split()
weights = [int(w) for w in weights]
capacity = int(input("Enter the capacity of knapsack:"))

# Maximum value calculation
max_value = knapsack_01(values, weights, capacity)
print("The maximum value that can be carried in the knapsack:", max_value)
