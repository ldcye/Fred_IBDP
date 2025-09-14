total = 0
name_arr = ["" for i in range(3)]
for i in range(3):
    name_arr[i] = input("Enter name: ")

score_arr = [[] for i in range(3)]
for i in range(3):
    for j in range(2):
        score = int(input("Enter score for " + name_arr[i] + ": "))
        total += score
        score_arr[i].append(score)
average = round(total / 3, 2)

# Create a proper 2D array for display
print_arr = [
    ["Student_name:", "Score1:", "Score2:"],
    [name_arr[0], score_arr[0][0], score_arr[0][1]],
    [name_arr[1], score_arr[1][0], score_arr[1][1]],
    [name_arr[2], score_arr[2][0], score_arr[2][1]]
]

# Display as a table
# print("\n" + "="*60)
print(f"{'Student Name':<15} {'Score 1':<8} {'Score 2':<8}")
# print("-"*60)

for i in range(3):
    print(f"{name_arr[i]:<15} {score_arr[i][0]:<8} {score_arr[i][1]:<8}")

print(f"\n{'Average':<15} {average:<8} {average:<8}")
print(f"{'Total':<15} {total:<8} {total:<8}")

# print("="*60)