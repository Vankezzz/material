import time
import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from config import *

# Создание подключения
params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)

# Создания канала с определенной очередью
channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=dlq_exchange,
    exchange_type='direct'
)
result = channel.queue_declare(
    queue=dlq_queue
)
channel.queue_bind(
    exchange=dlq_exchange,
    queue=dlq_queue,
    routing_key=dlq_routing_key
)


# Классический Callback
def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f" [x] Received {body.decode()} with delivery tag {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


consumer_tag = channel.basic_consume(
    queue=dlq_queue,
    on_message_callback=callback,
)
print(f"Запускаем потребителя с очередью {dlq_queue} на канале {consumer_tag}")
channel.start_consuming()
