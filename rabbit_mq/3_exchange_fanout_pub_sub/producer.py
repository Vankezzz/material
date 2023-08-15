import time
from config import *
import pika

ampq_url = 'amqp://guest:guest@almaz.loc:5672'
params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()
# ToDo для типа fanout нужно обьявить только exchange, все сообщения пойдут всем слушателям без ключа
channel.exchange_declare(exchange=exchange, exchange_type='fanout')
# channel.queue_declare(queue_1='task_queue', durable=True)  В таком типе соединения указывать не нужно!!!!

for i in range(100):
    message = f"Сообщение {i}"
    channel.basic_publish(
        exchange=exchange,
        routing_key='',  # В таком типе соединения указываем по-умолчанию
        body=message.encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(f" [x] Sent {message}")
    time.sleep(1)

blocking_conn.close()
