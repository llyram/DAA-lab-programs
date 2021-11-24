# Fraction knapsack problem in python 

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
    items.append({"ratio": val/wt, "weight": wt, "value": val})

# sorting the items according to ratio of value/weight
items = sorted(items, key=lambda i: i['ratio'], reverse=True)

# Adding the items to the knapsack
totalValue = 0
for i in items:
    curWt = i['weight']
    curVal = i['value']
    if capacity - curWt >= 0:
        capacity -= curWt
        totalValue += curVal
    else:
        break

print("Maximum possible value: " + str(totalValue))
