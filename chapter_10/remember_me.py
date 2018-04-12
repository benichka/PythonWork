# Simple program that store the user name in a file.
import json
username = input("What is your name?: ")

filename = "text_files/username.json"
with open(filename, 'w', encoding="utf-8") as tf:
    json.dump(username, tf)
    print("We'll remember you when you come back, " + username + "!")

