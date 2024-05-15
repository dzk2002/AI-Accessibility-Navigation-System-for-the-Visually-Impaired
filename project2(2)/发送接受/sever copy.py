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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
