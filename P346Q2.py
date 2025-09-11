arr = []
even = []

#user enter arr
num = int(input("Enter number of elements: "))
for i in range(0, num):
    ele = int(input("Enter element: "))
    arr.append(ele)

#find even 
for i in arr:
    if i % 2 == 0:
       even.append(i)
#find average
avg = sum(even)/len(even)
print (round(avg, 1))


odd = len(arr) - len(even)
print (odd)