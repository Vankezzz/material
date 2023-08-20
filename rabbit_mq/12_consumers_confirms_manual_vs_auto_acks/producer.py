import time
from config import *
import pika

params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)
channel = blocking_conn.channel()

for i in range(100):
    message = f"Сообщение {i}"
    channel.basic_publish(
        exchange=exchange,
        routing_key='',  # В таком типе соединения указываем по-умолчанию
        body=message.encode('utf-8')
    )
    print(f"Оправлено: {message}")
    time.sleep(1)

blocking_conn.close()
