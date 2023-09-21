import json

# Data to be written to the JSON file
data = {
    "name": "California",
    "population": 39538223,
    "capital": "Sacramento"
}

# Specify the file path where you want to save the JSON file
file_path = "california.json"

# Open the file in write mode ('w') and use 'json.dump' to write the data
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)  # 'indent' parameter for pretty formatting

print(f"JSON data has been written to {file_path}")

