#Construct code that allows the user to enter a noun and a letter. 
#Replace all occurrences of that letter with the "@" symbol.

noun = input("Enter a noun: ")
letter = input("Enter a letter: ")
modified_noun = noun.replace(letter, "@")
print(f"Modified noun: {modified_noun}")