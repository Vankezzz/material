import random
import time
import pika
from config import *

params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)
channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    exchange_type='direct'
)

for i in range(100):
    routing_key = random.choice([routing_key_1,routing_key_2])
    message = f"Сообщение {i} отправлено по ключу {routing_key}"
    channel.basic_publish(
        exchange=exchange,
        routing_key=routing_key,  # В таком типе соединения указываем по-умолчанию
        body=message.encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(f" [x] Sent {message}")
    time.sleep(1)

blocking_conn.close()
