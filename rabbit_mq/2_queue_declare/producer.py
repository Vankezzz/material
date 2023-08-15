import json

import pika

ampq_url = ''
exchange = ''
routing_key = ''
message = ''
params = pika.URLParameters(ampq_url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# durable=True - https://www.rabbitmq.com/tutorials/tutorial-two-python.html
channel.exchange_declare(
    exchange=exchange,
    durable=True,
    exchange_type="topic"
)

channel.basic_publish(
    exchange=exchange,
    routing_key=routing_key,
    body=json.dumps(message).encode('utf8')
)