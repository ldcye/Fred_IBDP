#quick sort implementation in python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    #Select an element from the array as the pivot(支点).
    pivot = arr[len(arr) // 2]
    
    #Partitioning step: reorder the array so that all elements 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    #With values less than the pivot come before the pivot
    #While all elements with values greater than the pivot come after it (equal values can go either way). 
    return quick_sort(left) + middle + quick_sort(right)

data = []
for _ in range(5):
    num = int(input("Enter a number: "))
    data.append(num)
print(quick_sort(data))