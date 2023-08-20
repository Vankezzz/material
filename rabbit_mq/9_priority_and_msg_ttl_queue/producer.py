import time
import pika
from config import *

params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()
for i in range(100):
    message = f"Сообщение {i}"
    channel.basic_publish(
        exchange=exchange,
        routing_key=queue,
        body=message.encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,  # сообщение в durable очереди запишется на диск
            priority=10 if i % 10 == 0 else 1
        )

    )
    print(f"Оправлено: {message}")
    time.sleep(1)

blocking_conn.close()
