import time

import pika

ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = ''
routing_key = ''
params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()

channel.queue_declare(queue='task_queue', durable=True)

for i in range(100):
    message = f"Сообщение {i}"
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message.encode('utf-8'),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ))
    print(f" [x] Sent {message}")
    time.sleep(1)

blocking_conn.close()