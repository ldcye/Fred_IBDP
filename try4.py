import string
import time

text = "Hello, World!"
temp = ""
for ch in text:
    for i in string.printable:
        if i == ch or ch == "":
            time .sleep(0.1)
            print(ch, end="")
            temp += ch
            break
        else:
            time .sleep(0.01)
            print (temp + i)