import time

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from config import *

params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()
channel.exchange_declare(
    exchange=exchange,
    durable=True,
)
channel.queue_declare(
    queue=queue,
    durable=True,
    arguments=
    {
        "x-message-ttl": 10000,  # Время жизни сообщения, в миллисекундах
        "x-max-priority": 10,    # Максимальный приоритет для очереди
        # "x-expires": 10,  # Если очередь не используется указанное тут время, то она удаляется

        # Режимы если queue переполнена
        # drop-head - удаляем старые сообщения, а новые вставляем в очередь
        # reject-publish - запрещаем пушить новые сообщения в очередь
        # reject-publish-dlx - запрещаем пушить новые сообщения в очередь, а они попадают в DLQ
        # "x-overflow": '',

        # Сколько максимум сообщений может держать очередь.
        # Остальные автоматически rejected
        # "x-max-length": 10,
        # Сколько максимум размера в памяти могут потреблять сообщения в очереди.
        # Остальные автоматически rejected
        # "x-max-length-bytes": 10,

        # "x-dead-letter-exchange": "",  # Название exchange, где находится DLQ
        # "x-dead-letter-routing-key": "",  # Routing key для DLQ

        # "x-queue-type": "",  # Вид очереди classic или quorum
    }
)
channel.queue_bind(
    exchange=exchange,
    queue=queue
)


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    print(
        f"Body: {body.decode()}; "
        f"Delivery tag: {method.delivery_tag};"
        f"Priority: {properties.priority};"
        f"TTL: {properties.expiration};"
    )
    # time.sleep(2)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
consumer_tag = channel.basic_consume(
    queue=queue,
    on_message_callback=callback
)
print(f"Запускаем потребителя с очередью {queue} на канале {consumer_tag}")

channel.start_consuming()
