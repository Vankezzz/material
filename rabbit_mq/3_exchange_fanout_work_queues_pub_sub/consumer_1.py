import time
import pika
from config import *

# Создание подключения
params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)

# Создания канала с определенной очередью
channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    exchange_type='fanout'
)
result = channel.queue_declare(
    queue=queue_1,
)
channel.queue_bind(
    exchange=exchange,
    queue=queue_1
)


# Классический Callback
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


consumer_tag = channel.basic_consume(
    queue=queue_1,
    on_message_callback=callback,
)
print(f"Запускаем потребителя с очередью {queue_1} на канале {consumer_tag}")
channel.start_consuming()
