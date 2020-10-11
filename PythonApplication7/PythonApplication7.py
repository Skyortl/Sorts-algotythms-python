from datetime import datetime
import random
import numpy
def bucketSort(input_list):
    max_value = numpy.max(input_list)
    size = max_value/len(input_list)

    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:

        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

items = []
min = 50000
max = 1000000
step = 50000
while min <= max:
    items =  [random.randint(0, 100000) for i in range(min)]
    startTime = datetime.now()
    bucketSort(items)
    print('bucketSort {}'.format(datetime.now() - startTime), 'elements {}'.format(min))
    items = [random.randint(0, 100000) for i in range(min)]
    startTime = datetime.now()
    shellSort(items, len(items))
    print('shellSort {}'.format(datetime.now()-startTime),'elements {}'.format(min))
    items = [random.randint(0, 100000) for i in range(min)]
    startTime = datetime.now()
    quickSort(items, 0, len(items) - 1)
    print('quickSort {}'.format(datetime.now()-startTime),'elements {}'.format(min))
    min = min + step


