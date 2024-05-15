from aip import AipImageClassify
import logging
APP_ID = '68096498'
API_KEY = '78A1sSgNxE3f7rjX2bDQaYyS'
SECRET_KEY = '4KLDckV1FcoWv3gnAFFtHlydZMMMYMfI'


def recognize_image(image_path):
    try:
        client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
        with open(image_path, 'rb') as f:
            image_data = f.read()

        options = {'baike_num': 5}
        res = client.advancedGeneral(image_data, options=options)

        if 'result' in res:
            return [item['keyword'] for item in res['result'][:6]]
        else:
            return []
    except Exception as e:
        logging.error(f"Image recognition failed: {e}")
        return []
