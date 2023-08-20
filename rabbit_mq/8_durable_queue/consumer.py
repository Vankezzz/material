import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from config import *

params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    durable=True
)
channel.queue_declare(
    queue=queue,
    durable=True
)
channel.queue_bind(
    exchange=exchange,
    queue=queue
)


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"Body: {body.decode()}; "
          f"Delivery tag: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


consumer_tag = channel.basic_consume(
    queue=queue,
    on_message_callback=callback
)
print(f"Запускаем потребителя с очередью {queue} на канале {consumer_tag}")

channel.start_consuming()
