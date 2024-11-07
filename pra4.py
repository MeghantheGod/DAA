class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractionalknap(w, arr):
    # Sort items by profit-to-weight ratio in descending order
    arr.sort(key=lambda x: x.profit / x.weight, reverse=True)
    final_value = 0
    
    for item in arr:
        # If item can be picked whole
        if w >= item.weight:
            final_value += item.profit
            w -= item.weight
        else:
            # Take the fraction of the item that fits
            final_value += item.profit * (w / item.weight)
            break
    return final_value

if __name__ == '__main__':
    n = int(input("Enter the total number of items:\n"))
    arr = []
    for i in range(n):
        profit = int(input(f"Enter the profit of item {i+1}:\n"))
        weight = int(input(f"Enter the weight of item {i+1}:\n"))
        arr.append(Item(profit, weight))
    
    w = int(input("Enter the maximum weight of the knapsack:\n"))
    print("Maximum profit from the items:", fractionalknap(w, arr))

