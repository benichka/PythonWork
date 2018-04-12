# Simple program that reads data from a JSON file.
import json
text_file = "text_files/numbers.json"

with open(text_file, 'r', encoding="utf-8") as tf:
    numbers = json.load(tf)

print(numbers)
