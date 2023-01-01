#Insrt Sort
def Insert_sort(arr, acse = True) :
    for i in range (1, len(arr)) :
        key = arr[i]
        j = i - 1
        while j >= 0 :
            if acse and arr[j] < key :
                break
            if not acse and arr[j] > key :
                break
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

#Test code
import random
arr = [random.randint(1, 100) for _ in range(10)]
print(arr)
print(Insert_sort(arr, False))