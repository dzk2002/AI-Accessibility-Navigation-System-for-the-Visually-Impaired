from app import create_app
from app.globals import current_distance
from app.routes import update_current_message
from utils.camera import fetch_image_and_distance
from services.image_recognition import recognize_image
from threading import Thread
import time
import os
import logging

from app import globals


def periodic_task(pic_dir, distance_file):
    while True:
        logging.info("Starting the image recognition task...")

        fetch_image_and_distance(pic_dir)

        image_path = os.path.join(pic_dir, 'latest_image.jpg')
        if globals.should_recognize_image:

            keywords = recognize_image(image_path)
            message = f'Keywords: {", ".join(keywords)} Distance:{", ".join(current_distance)}'

            update_current_message(message)

            logging.info(message)

            globals.should_recognize_image = False  # Reset the flag after recognition

        time.sleep(1)


if __name__ == '__main__':
    app = create_app()

    # 设置日志
    logging.basicConfig(level=logging.INFO)

    # 创建后台线程进行周期性任务
    pic_dir = 'static/images'
    thread = Thread(target=periodic_task, args=pic_dir)
    thread.daemon = True
    thread.start()

    # 启动 Flask 应用
    app.run(host='0.0.0.0', port=5000)
