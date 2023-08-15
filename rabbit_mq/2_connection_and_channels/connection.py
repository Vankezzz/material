import pika

ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = ''
routing_key = ''
params = pika.URLParameters(ampq_url)

blocking_conn = pika.BlockingConnection(params)
a = 0
