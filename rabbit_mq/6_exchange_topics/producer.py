import random
import time
from config import *
import pika

params = pika.URLParameters(ampq_url)
with pika.BlockingConnection(params) as blocking_conn:
    channel = blocking_conn.channel()

    for i in range(100):
        routing_key = random.choice(routing_keys)
        message = f"Сообщение {i} отправлено по ключу {routing_key}"
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,  # В таком типе соединения указываем по-умолчанию
            body=message.encode('utf-8')
        )
        print(f"Оправлено: {message}")
        time.sleep(1)

    blocking_conn.close()
