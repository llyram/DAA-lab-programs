#!/bin/python

def subset(sum, i, count):
    if sum == d:
        display(count)
        return

    if (sum > d) or (i >= len(array)):
        return

    else:
        # print(i)
        set[count] = array[i]

        count += 1
        subset(sum + array[i], i+1, count)
        count -= 1
        subset(sum, i+1, count)


def display(c):
    if c == 0:
        print("No subsets were found")
        return
    print("{", end="")
    for i in range(c):
        print(set[i], end="")
    print("}")


if __name__ == "__main__":
    set = [0]*10

    # array = [1, 2, 5, 6, 8]
    array = list(map(int,input("\nEnter elements of array : ").split()))
    d = int(input("Enter the value of d: "))
    count = 0
    subset(0, 0, 0)
