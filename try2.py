# Selection Sort Implementation in Python

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

data = []
for _ in range(5):
    num = int(input("Enter a number: "))
    data.append(num)
print(selection_sort(data))