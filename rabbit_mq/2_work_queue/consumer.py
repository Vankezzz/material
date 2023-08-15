import time

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = ''
routing_key = ''
params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()

channel.queue_declare(
    queue='task_queue',
    durable=True  # ToDo обьяснить
)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f" [x] Received {body.decode()} with delivery tag {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue='task_queue',
    on_message_callback=callback
)

channel.start_consuming()
