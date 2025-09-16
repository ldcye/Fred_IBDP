import random
matrix = [[0 for i in range(4)]for i in range(6)]
for i in range (4):
    for j in range (6):
        matrix.append(random.randint(1,10))
print (matrix)