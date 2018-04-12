# Simple program that reads the username from a file and greet the user.
import json

filename = "text_files/username.json"

with open(filename, 'r', encoding="utf-8") as tf:
    username = json.load(tf)
    print("Welcome back, " + username + "!")
