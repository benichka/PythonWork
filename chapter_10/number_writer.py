# Simple program that store data to a JSON file.
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "text_files/numbers.json"
with open(filename, 'w', encoding="utf-8") as text_file:
    json.dump(numbers, text_file)
