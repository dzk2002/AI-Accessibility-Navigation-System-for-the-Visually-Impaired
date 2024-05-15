from flask import Flask, jsonify
from threading import Lock
import time

app = Flask(__name__)
file_lock = Lock()
last_message = ""
last_read_time = 0

@app.route('/get_message')
def get_first_message():
    global last_message
    global last_read_time
    try:
        # 检查上次读取时间，如果超过5秒就重新读取，否则保持不变
        if time.time() - last_read_time > 5:
            with file_lock:
                with open('messages.txt', 'r', encoding='utf-8') as file:
                    last_message = file.readline().strip()
            last_read_time = time.time()
        return jsonify({'message': last_message})
    except FileNotFoundError:
        return jsonify({'error': 'Messages file not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
