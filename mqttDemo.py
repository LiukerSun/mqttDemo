import paho.mqtt.publish as publish
import random
import time

# MQTT 配置
broker = "localhost"  # 或者你的 MQTT 代理地址
port = 1883
topic = "sensor/data"


# 生成并发送模拟数据的函数
def publish_fake_sensor_data():
    while True:
        messages = []
        for _ in range(1000):  # 生成一批 1000 条消息
            # 生成模拟数据，例如温度和湿度
            temperature = random.uniform(20, 30)  # 生成 20 到 30 之间的随机温度
            humidity = random.uniform(40, 60)  # 生成 40 到 60 之间的随机湿度

            # 创建消息内容
            payload = f"sensor_data temperature={temperature},humidity={humidity}"
            messages.append({"topic": topic, "payload": payload})

        # 批量发布消息
        publish.multiple(messages, hostname=broker, port=port)

# 运行函数以开始发送模拟数据
publish_fake_sensor_data()
