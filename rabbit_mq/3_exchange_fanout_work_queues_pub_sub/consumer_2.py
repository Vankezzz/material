import time
import pika
from pika.amqp_object import Method

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
result: Method = channel.queue_declare(
    queue=queue_2,
)
channel.queue_bind(
    exchange=exchange,
    queue=queue_2
)


# Классический Callback
def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")


consumer_tag = channel.basic_consume(
    queue=queue_2,
    on_message_callback=callback,
)
print(f"Запускаем потребителя с очередью {queue_2} на канале {consumer_tag}")
channel.start_consuming()
