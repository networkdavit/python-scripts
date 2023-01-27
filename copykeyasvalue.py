import json

# Load the JSON file
with open('default.json', 'r') as f:
    data = json.load(f)

# Update the values to be the same as the keys
for key in data:
    data[key] = key

# Write the updated JSON to a new file
with open('en.json', 'w') as f:
    json.dump(data, f, indent=4)