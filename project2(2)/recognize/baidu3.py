from aip import AipImageClassify
import logging
from googletrans import Translator

APP_ID = '68096498'
API_KEY = '78A1sSgNxE3f7rjX2bDQaYyS'
SECRET_KEY = '4KLDckV1FcoWv3gnAFFtHlydZMMMYMfI'

def translate_text(text):
    translator = Translator()
    translated = translator.translate(text, dest='en')
    return translated.text

def recognize_image(image_path):
    try:
        client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        with open(image_path, 'rb') as f:
            image_data = f.read()

        options = {'baike_num': 5}
        res = client.advancedGeneral(image_data, options=options)

        if 'result' in res:
            keywords = [item['keyword'] for item in res['result'][:6]]
            # keywords2 = translate_text(keywords)
            return keywords
        else:
            print("未能识别出图片中的内容。")
    except Exception as e:
        logging.error(f"图片识别失败：{e}")

# 使用示例
image_path = r'C:\Users\10710\Desktop\CPS4951\Second project\project2\recognize\5.jpg'  # 替换为你的图片路径
print(recognize_image(image_path))
print(translate_text("你好"))
