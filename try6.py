user_name = input("Enter your player name: ")

user_mane = user_name.replace(" ","")
if "admin" in user_name.lower():
    user_name = user_name.lower().replace("admin","player")
user_name = user_name.replace("\n","").replace("\t","")
user_name = user_name.find("_")
if user_name == -1:
    clan_name = "NoClan"
else:
    first_underscore = user_name.find("_")
    last_underscore = user_name.rfind("_")
    clan_name = user_name[first_underscore + 1:last_underscore]
print ("Your clan name is: ",clan_name)
print ("Your username has ",len(user_name.split("_"))," parts.")
user_name = user_name + "_gamer"
print ("The first character of your username is: ",user_name[0])
print ("The last character of your username is: ",user_name[-1])