import time
from config import *
from utils import *

params = create_tls_connection_params(host, tls_port,user,password,ca_cert_path,client_cert_path,client_key_path,secret)

with pika.BlockingConnection(params) as conn:
    channel = conn.channel()
    for i in range(100):
        message = f"Сообщение {i}"
        channel.basic_publish(
            exchange=exchange,
            routing_key=queue,
            body=message.encode('utf-8'),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # сообщение в durable очереди запишется на диск
            )

        )
        print(f"Оправлено: {message}")
        time.sleep(1)

