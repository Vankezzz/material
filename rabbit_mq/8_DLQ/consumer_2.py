import time
import pika
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic

from config import *

# Создание подключения
params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)

# Создания канала с определенной очередью
channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    exchange_type='direct'
)
result = channel.queue_declare(
    queue=queue_1,
    arguments={
        'x-message-ttl': 1000,
        "x-dead-letter-exchange": dlq_exchange,
        "x-dead-letter-routing-key": dlq_routing_key,  # if not specified, queue's routing-key is used
    }
)
channel.queue_bind(
    exchange=exchange,
    queue=queue_1,
    routing_key=routing_key
)


# Классический Callback
def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f" [x] Received {body.decode()} with delivery tag {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


consumer_tag = channel.basic_consume(
    queue=queue_1,
    on_message_callback=callback,
)
print(f"Запускаем потребителя с очередью {queue_1} на канале {consumer_tag}")
channel.start_consuming()
