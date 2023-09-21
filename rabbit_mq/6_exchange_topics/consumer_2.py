import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.exchange_type import ExchangeType
from pika.spec import Basic, BasicProperties

from config import *


# Классический Callback
def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"Body: {body.decode()}; "
          f"Delivery tag: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Создание подключения
params = pika.URLParameters(ampq_url)
with pika.BlockingConnection(params) as blocking_conn:
    # Создания канала с определенной очередью
    channel = blocking_conn.channel()
    channel.exchange_declare(
        exchange=exchange,
        exchange_type=ExchangeType.topic
    )
    result = channel.queue_declare(
        queue='',
        exclusive=True
    )
    queue_name = result.method.queue

    channel.queue_bind(
        exchange=exchange,
        queue=queue_name,
        routing_key=binding_key_2
    )
    consumer_tag = channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
    )
    print(f"Запускаем потребителя с очередью {queue_name} на канале {consumer_tag} c binding: {binding_key_2}")
    channel.start_consuming()
