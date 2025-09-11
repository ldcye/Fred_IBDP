# Username processor for students

def process_username(raw_username: str) -> None:
    # 1) Trim spaces at both ends
    username = raw_username.strip()

    # 2) Replace "admin" with "player"
    if "admin" in username:
        username = username.replace("admin", "player")

    # 3) Remove escape sequences: actual and literal \n/\t
    username = username.replace("\n", "").replace("\t", "")
    username = username.replace("\\n", "").replace("\\t", "")

    # 4) Find first and last underscore to compute clan name
    first_us = username.find("_")
    last_us = username.rfind("_")
    if first_us != -1 and last_us != -1 and first_us < last_us:
        clan_name = username[first_us + 1:last_us]
    else:
        clan_name = "NoClan"

    # 5) Split by underscore and count parts
    parts = username.split("_") if username else []
    num_parts = len(parts)

    # 6) Concatenate with _Gamer
    final_username = f"{username}_Gamer"

    # 7) First and last characters of final username
    if final_username:
        first_char = final_username[0]
        last_char = final_username[-1]
    else:
        first_char = ""
        last_char = ""

    # Display results
    print("Processed Username:", username)
    print("Clan Name:", clan_name)
    print("Parts Count:", num_parts)
    print("Final Username:", final_username)
    print("First Char:", first_char)
    print("Last Char:", last_char)


if __name__ == "__main__":
    user_input = input("Enter username: ")
    process_username(user_input)


