#Construct code that allows the user to enter their first and last names. 
#Concatenate the two values, add a space in between and display the full name together with its length without the space.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
length_without_space = len(first_name) + len(last_name)
print(f"Full name: {full_name}")
print(f"Length of full name without space: {length_without_space}")