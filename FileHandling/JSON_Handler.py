import json

class JSONHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
        return data

    def write_json(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("JSON file has been written successfully.")

json_handler = JSONHandler('data.json')

# Read JSON file
json_data = json_handler.read_json()
print("JSON Data:")
print(json_data)

# Write JSON file
new_data = [
    {
        "name": "Sarah",
        "age": 34,
        "city": "Dallas"
    },
    {
        "name": "Daniel",
        "age": 27,
        "city": "Phoenix"
    }
]
json_handler.write_json(new_data)

# Read JSON file after writing
updated_json_data = json_handler.read_json()
print("\nUpdated JSON Data:")
print(updated_json_data)
