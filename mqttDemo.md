```shell
docker run -d --name nanomq -p 1883:1883 -p 8083:8083 -p 8883:8883 emqx/nanomq:0.20

docker run -itd --name influxdb -p 8086:8086 influxdb:2.5.1

docker network create db_network
docker network connect db_network influxdb
docker network connect db_network nanomq
```



```shell
docker run -d --name telegraf --network db_network -v $PWD/telegraf.conf:/etc/telegraf/telegraf.conf:ro telegraf
```







一个python脚本模拟传感器

```python
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
        # 生成模拟数据，例如温度和湿度
        temperature = random.uniform(20, 30)  # 生成 20 到 30 之间的随机温度
        humidity = random.uniform(40, 60)  # 生成 40 到 60 之间的随机湿度

        # 创建消息内容
        payload = f"temperature={temperature},humidity={humidity}"

        # 发布消息
        publish.single(topic, payload, hostname=broker, port=port)

        # 每隔一秒发送一次数据
        time.sleep(1)


# 运行函数以开始发送模拟数据
publish_fake_sensor_data()

```
