from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from config import *
import pika

params = pika.URLParameters(ampq_url)
blocking_conn = pika.BlockingConnection(params)
channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    exchange_type='direct'
)
result = channel.queue_declare(
    queue='',
    exclusive=True
)
queue_name = result.method.queue
channel.queue_bind(
    exchange=exchange,
    queue=queue_name,
    routing_key=routing_key_2
)


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f" [x] Received {body.decode()} with delivery tag {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


consumer_tag = channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
)
print(f"Запускаем потребителя с очередью {queue_name} на канале {consumer_tag} с binding key {routing_key_2}")
channel.start_consuming()
