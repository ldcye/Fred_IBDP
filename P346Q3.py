# create a array with 16 integers
arr = [16,93,73,84,12,38,25,56,97,64,49,71,82,11,29,45]
reverse_arr = []
temp = 0

for i in range(len(arr)):
    reverse_arr.append(arr[len(arr)-1-i])
print (reverse_arr)