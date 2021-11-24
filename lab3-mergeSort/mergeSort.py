import random
import time
import matplotlib.pyplot as plt

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements into two halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



# Driver Code
if __name__ == '__main__':
    n_values = []
    n_time = []
    for n in range( 5000, 30000, 1000):
        rand_arr = [random.randint(1, 1000000) for _ in range(n)]

        # timing the merge sort function
        start = time.time()
        mergeSort(rand_arr)
        end = time.time()

        n_values.append(n)
        n_time.append(end-start)

        print("Time taken to sort array of " + str(n) + " numbers: " + str(end-start) + "s")
    
    plt.plot(n_values, n_time)
    plt.title("Merge Sort")
    plt.xlabel("values of N")
    plt.ylabel("execution time")
    plt.show()

    
