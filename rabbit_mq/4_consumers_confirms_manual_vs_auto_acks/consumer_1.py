import logging
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
    exchange_type='fanout'
)
result = channel.queue_declare(
    queue=queue_1,
)
channel.queue_bind(
    exchange=exchange,
    queue=queue_1
)


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(f" [x] Received {body.decode()} with delivery tag {method.delivery_tag}")
    if method.delivery_tag % 10 == 0:
        raise Exception("Случилась ошибка")


consumer_tag = channel.basic_consume(
    queue=queue_1,
    on_message_callback=callback,
    auto_ack=False  # "fire-and-forget" - автоматическое подтверждение работает так,
    # что положительный ack отсылается после доставки потребителю сообщения
)
print(f"Запускаем потребителя с очередью {queue_1} на канале {consumer_tag}")
channel.start_consuming()
