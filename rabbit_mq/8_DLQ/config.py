ampq_url = 'amqp://guest:guest@almaz.loc:5672'

exchange = '8_DLQ'
queue_1 = 'consumer_1'
routing_key = 'task_queue'

dlq_exchange = '8_DLQ_dlq'
dlq_queue = 'dlq_consumer_2'
dlq_routing_key = 'dlq_task_queue'
