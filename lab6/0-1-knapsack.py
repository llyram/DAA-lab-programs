#!/bin/python
items = []

# Taking input values
print("Enter knapsack capacity: ", end="")
capacity = int(input())
print("")

print("Enter number of items: ", end="")
n = int(input())
print("")

for i in range(n):
    print("Enter weight of item " + str(i+1) + ": ", end="")
    wt = int(input())
    print("Enter value of item " + str(i+1) + ": ", end="")
    val = int(input())
    print("")
    items.append({"weight": wt, "value": val})

K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

# Build table K[][] in bottom up manner
for i in range(n + 1):
	for w in range(capacity + 1):
		if i == 0 or w == 0:
			K[i][w] = 0
		elif items[i-1]['weight'] <= w:
			K[i][w] = max(items[i-1]['value'] + K[i-1][w-items[i-1]['weight']], K[i-1][w])
		else:
			K[i][w] = K[i-1][w]

print("Maximum possible value: " + str(K[n][capacity]))
