from flask import Flask, render_template, jsonify
import time
import json
from helpers.file_utils import read_status_from_file, write_status_to_file, load_json_file

app = Flask(__name__, template_folder="../templates")

config = load_json_file("../config/config.json")
status_file_path = "../config/status.json"

@app.route(f"/{config['get']}", methods=['GET'])
def handle_motion_request():
    global last_detection_time
    last_detection_time = time.time()
    write_status_to_file(status_file_path, True, "Room is Open")
    return "Motion Detection Running"

@app.route(f"/{config['status']}", methods=['GET'])
def handle_status_request():
    status, content = read_status_from_file(status_file_path)
    return jsonify({"status": status, "content": content})

@app.route('/')
def index():
    _, content = read_status_from_file(status_file_path)
    return render_template('index.html', content=content)

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])
