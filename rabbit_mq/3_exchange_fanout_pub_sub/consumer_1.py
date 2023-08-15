import time

import pika

ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = ''
routing_key = ''
params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)

channel = blocking_conn.channel()
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout' # ToDo
)
result = channel.queue_declare(
    queue='',
    exclusive=True   # ToDo обьяснить
)
queue_name = result.method.queue_1

channel.queue_bind(
    exchange='logs',
    queue=queue_name
)

print(f'Queue:{queue_name} Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    # auto_ack=True  # ToDo обьяснить
)

channel.start_consuming()
