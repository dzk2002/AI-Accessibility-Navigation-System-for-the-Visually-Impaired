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
            translated_keywords = [translate_text(keyword) for keyword in keywords]
            print("Translated Results:")
            for keyword in translated_keywords:
                print(keyword)
        else:
            print("No results found.")
    except Exception as e:
        logging.error(f"Image recognition failed: {e}")

# Example usage:
image_path = r'C:\Users\10710\Desktop\CPS4951\Second project\project2\recognize\5.jpg'

translated_keywords = recognize_image(image_path)

print("Translated keywords:", translated_keywords)