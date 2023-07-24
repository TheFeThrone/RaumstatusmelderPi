import json

def write_status_to_file(file_path, status, content):
    data = {"status": status, "content": content}
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)

def read_status_from_file(file_path):
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            return data.get("status", False), data.get("content", "Content not found")
    except FileNotFoundError:
        return False, "File not found"

def load_json_file(file_path):
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}
