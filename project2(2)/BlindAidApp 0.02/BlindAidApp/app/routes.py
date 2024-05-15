from flask import render_template, request, jsonify
import logging
messages = []
from . import globals
current_message = ''
def init_routes(app):
    @app.route('/')
    def index():
        return render_template('phone_display.html')

    @app.route('/send_to_phone', methods=['POST'])
    def send_to_phone():
        try:
            data = request.json
            messages.append(data['message'])
            logging.info(f"Message received and stored: {data['message']}")
            return jsonify({'status': 'Message sent successfully'})
        except Exception as e:
            logging.error(f"Failed to store message: {e}")
            return jsonify({'status': 'Error'}), 500

    @app.route('/receive_messages')
    def receive_messages():
        return jsonify({'messages': current_message})

    @app.route('/current_info')
    def current_info():
        return jsonify({'message': current_message})



    @app.route('/acknowledge_speech_end', methods=['POST'])
    def acknowledge_speech_end():
        globals.should_recognize_image = True
        logging.info("Speech end acknowledged.")
        return jsonify({'status': 'Acknowledged'})


def update_current_message(message):
    global current_message
    current_message = message