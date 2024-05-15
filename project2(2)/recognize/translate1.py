import requests
import hashlib
import random

def translate_text(text):
    """调用百度翻译API进行翻译"""
    appid = '20240508002045788' 
    secretKey = 'eCI0r5qIMXeL1x3vTnq9' 
    
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    params = {
        'q': text,
        'from': 'zh',
        'to': 'en',
        'appid': appid,
        'salt': salt,
        'sign': sign
    }
    response = requests.get(url, params=params)
    result = response.json()
    
    if 'trans_result' in result:
        return result['trans_result'][0]['dst']
    else:
        return "翻译失败"

# Main function
if __name__ == '__main__':
    text_to_translate = "你好"
    translated_text = translate_text(text_to_translate)
    print("Translated text:", translated_text)
