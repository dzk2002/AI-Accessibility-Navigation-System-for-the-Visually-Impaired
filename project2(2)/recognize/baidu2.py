from aip import AipImageClassify
import re

def picdata(image_path):
    """ 图像识别 """
    APP_ID = '67896977'
    API_KEY = 'JV2q3NkQ3v8UUx5y2hVoYdoI'
    SECRET_KEY = 'VwjzKOP7lPEhpsgCNYIIXWfH8xCOWLUt'
    client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    
    # Read image file content
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Call image classification API
    options = {'baike_num': 5}
    res = client.advancedGeneral(image_data, options=options)

    # Extract and print recognition results
    print('\033[1;33m\n----------------------\n图像识别结果:\n----------------------')
    first_result = res['result'][0]  # 获取第一行数据
    words = re.findall(r'\b\w+\b', first_result['keyword'])  # 提取第一行数据中的单词
    print(' '.join(words[:5]))  # 输出第一行数据中的前五个单词

# Main function
if __name__ == '__main__':
    image_path = r"C:\Users\10710\Desktop\CPS4951\Second project\project2\recognize\7.jpg"
    picdata(image_path)
