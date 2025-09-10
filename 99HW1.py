#Construct code that asks the user to provide their name, house / flat number and their street number or name..
#Concatenate this information to display a message such as the following.
#(Attempt to write the message by using one single line of code, and ensure it is displayed on two separate lines, as shown.)
#From: Name
#Address: Full Address
#Message:Why was there a bug in the computer? Because it was looking for a "byte” to eat!

name = input("Enter your name: ")
house_number = input("Enter your house/flat number: ")
street_name = input("Enter your street name or number: ")

print(f"From: {name}\nAddress: {house_number} {street_name}\nMessage:\nWhy was there a bug in the computer? Because it was looking for a 'byte' to eat!")