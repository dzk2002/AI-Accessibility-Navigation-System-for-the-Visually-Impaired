from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # 导入 CORS

app = Flask(__name__)
CORS(app)  # 启用 CORS

# 现存的路由和应用逻辑
messages = []

@app.route('/')
def index():
    return render_template('send_to_phone.html')


@app.route('/send_to_phone', methods=['POST'])
def send_to_phone():
    data = request.json
    messages.append(data['message'])
    return jsonify({'status': 'Message sent successfully'})

@app.route('/receive_messages')
def receive_messages():
    return jsonify({'messages': messages})

@app.route('/get_messages')
def get_messages():
    # 假设您的消息保存在当前目录下的 messages.txt 文件中
    try:
        with open('messages.txt', 'r') as file:
            messages = file.readlines()
        # 去除每行末尾的换行符并返回
        messages = [message.strip() for message in messages]
        return jsonify({'messages': messages})
    except FileNotFoundError:
        return jsonify({'error': 'Messages file not found'}), 404

@app.route('/add_message', methods=['POST'])
def add_message():
    new_message = request.json.get('message')
    if not new_message:
        return jsonify({'error': 'No message provided'}), 400
    try:
        with open('messages.txt', 'a') as file:
            file.write(f"{new_message}\n")
        return jsonify({'status': 'Message added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
