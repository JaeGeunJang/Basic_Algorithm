#Bubble Sort Code
def bubble_sort(arr, asce=True) :
    for i in range(len(arr)-1) :
        for j in range(1, len(arr)-i) :
            if asce :
                if arr[j-1] > arr[j] :
                    arr[j-1], arr[j] = arr[j], arr[j-1]
            else :
                if arr[j-1] < arr[j] :
                    arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

#Test Code
import random
arr = [random.randint(1, 100) for _ in range(10)]
print(arr)
print(bubble_sort(arr))
print(bubble_sort(arr, False))