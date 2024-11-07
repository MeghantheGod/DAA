def fractional_knap(value,weight,capacity):
	ratio = [v/w for v,w in zip(value,weight)]
	index = list(range(len(value)))
	index.sort(key=lambda i:ratio[i], reverse=True)
	max_value = 0
	fractions = [0]*len(value)
	
	for i in index:
		if weight[i] <= capacity:
			fractions[i] = 1
			max_value += value[i]
			capacity -= weight[i]
		else:
			fractions[i] = capacity/weight[i]
			max_value += value[i] * capacity / weight[i]
			break
	return max_value,fractions
	
n = int(input("Enter the total number of items:"))
value = input("Enter the value of the item{} in order:".format(n)).split()
value = [int(v) for v in value]
weight = input("Enter the weight of the item{} in order:".format(n)).split()
weight = [int(w) for w in weight]
capacity = int(input("Enter the capacity of knapsack:"))
max_value,fractions = fractional_knap(value,weight,capacity)
print("The maximum value in which the items can be carried:", max_value)
print("The fraction of items that can be carried:", fractions)
