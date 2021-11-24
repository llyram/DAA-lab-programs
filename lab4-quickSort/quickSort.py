import random
import time
import matplotlib.pyplot as plt

def partition(start, end, array):
      
    pivot_index = start 
    pivot = array[pivot_index]
      
    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1
          
        if(start < end):
            array[start], array[end] = array[end], array[start]


    array[end], array[pivot_index] = array[pivot_index], array[end]
     
    return end


def quickSort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)


if __name__ == '__main__':
    n_values = []
    n_time = []
    # quickSort(0, 6, [1,9,6,0,3,5,5])
    for n in range( 5000, 31000, 1000):
        rand_arr = [random.randint(1, 1000000) for _ in range(n)]

        # timing the merge sort function
        start = time.time()
        quickSort(0, n-1, rand_arr)
        end = time.time()

        n_values.append(n)
        n_time.append(end-start)

        print("Time taken to sort array of " + str(n) + " numbers: " + str(end-start) + "s")
    
    plt.plot(n_values, n_time)
    plt.title("Quick Sort")
    plt.xlabel("values of N")
    plt.ylabel("execution time")
    plt.show()

    
