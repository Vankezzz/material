from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from config import *
from utils import *

params = create_tls_connection_params(host, tls_port,user,password,ca_cert_path,client_cert_path,client_key_path,secret)


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f"Body: {body.decode()}; "
          f"Delivery tag: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


with pika.BlockingConnection(params) as conn:
    channel = conn.channel()
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

    consumer_tag = channel.basic_consume(
        queue=queue,
        on_message_callback=callback
    )
    print(f"Запускаем потребителя с очередью {queue} на канале {consumer_tag}")
    channel.start_consuming()

