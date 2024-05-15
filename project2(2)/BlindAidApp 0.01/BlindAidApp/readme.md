BlindAidApp/
│
├── app/
│   ├── __init__.py
│   ├── routes.py        # 处理Flask路由的配置
│   ├── config.py        # 设置Flask的配置参数
│
├── services/
│   ├── image_recognition.py   # 封装百度图像识别服务
│   ├── message_handler.py     # 用于处理和存储信息
│
├── models/
│   ├── models.py        # 数据模型，例如消息存储结构
│
├── static/
│   └── images/          # 存放从ESP32-CAM获取的图像
│
├── templates/
│   └── phone_display.html  # 显示信息的HTML模板
│
├── utils/
│   ├── camera.py        # 与ESP32-CAM交互获取图像和距离
│
├── run.py               # 启动Flask应用程序的主文件
│
└── requirements.txt     # 项目依赖的Python库列表

从anaconda导入blindAid.yaml
