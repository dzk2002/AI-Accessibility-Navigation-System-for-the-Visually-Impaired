import os
import requests
import time
import logging

import app.globals

ESP32_CAM_URL = "http://192.168.43.239"  # 根据实际情况修改 IP 地址

def fetch_image_and_distance(pic_dir, distance_file):
    os.makedirs(pic_dir, exist_ok=True)
    attempts = 0
    success = False

    while not success and attempts < 5:
        try:
            pic_response = requests.get(f"{ESP32_CAM_URL}/picture", timeout=5)
            pic_path = os.path.join(pic_dir, 'latest_image.jpg')
            with open(pic_path, 'wb') as f:
                f.write(pic_response.content)
            logging.info("Image fetched successfully.")

            distance_response = requests.get(f"{ESP32_CAM_URL}/distance", timeout=5)
            distance_cm = parse_distance(distance_response.text)
            with open(distance_file, 'w') as f:
                f.write(str(distance_cm))
            logging.info(f"Distance fetched successfully: {distance_cm} cm")
            success = True
        except requests.exceptions.RequestException as e:
            attempts += 1
            logging.error(f"Attempt {attempts}: Failed to fetch data. Error: {e}")
            time.sleep(1)

    if not success:
        logging.error("Failed to fetch data after several attempts.")



def parse_distance(distance_text):
    if 'Distance: ' in distance_text and 'mm' in distance_text:
        return int(distance_text.split(':')[1].split('mm')[0].strip()) // 10  # 转换为厘米
    return -1  # 如果距离信息无效则返回 -1
