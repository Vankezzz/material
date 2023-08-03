import socket
from typing import List

from confluent_kafka import Consumer, TopicPartition, Producer

from config import bootstrap_servers, consumers_group_id_1, topic_1, dlq_topic


def print_assignment(consumer: Consumer, partitions: List[TopicPartition]):
    if partitions:
        print('Назначили партиции:', partitions)
    else:
        print("Партиция простаивает")


def print_revoke(consumer, partitions):
    print('Revoke:', partitions)


def print_lost(consumer, partitions):
    print('Lost:', partitions)


def create_producer(servers: str, topic: str) -> Producer:
    conf = {
        # Mandatory
        'bootstrap.servers': bootstrap_servers,
        'client.id': socket.gethostname(),
        # Optional
    }
    producer: Producer = Producer(**conf)
    return producer


def consume(servers: str, group_id: str, topic: str, dlq_producer: Producer):
    # Конфигурация и создание consumer
    consumer_config = {
        # Mandatory параметры
        'bootstrap.servers': servers,
        'group.id': group_id
    }
    consumer = Consumer(consumer_config)

    # Подписываемся на topic и обрабатываем сообщения
    try:

        consumer.subscribe(
            [topic],
            on_assign=print_assignment,
            on_revoke=print_revoke,
            on_lost=print_lost
        )

        # В цикле запрашиваем новые данные(пачки) от kafka с помощью poll()
        while True:
            # Ждет 1 секунду, пока появятся записи, если не получил в течении этого времени, то возвращает None
            message = consumer.poll(timeout=1.0)

            if not message:
                continue
            if message.error():
                print(f'Ошибка вовремя consuming: {message.error()}')
            else:
                print(
                    f'Received message: {message.value().decode("utf-8")} '
                    f'from {message.topic()} [{message.partition()}] '
                    f'at offset {message.offset()}'
                )
                if message.value().decode("utf-8") == "error":
                    raise Exception("мы его сломали")
    except Exception as ex:
        dlq_producer.produce(dlq_topic, value=str(ex))
        dlq_producer.flush()
    finally:
        # Note 1: Закрытие открытых сокетов
        # Note 2: Вызывает ре-балансировку группы
        # Если не вызвать принудительно, то kafka будет ждать истечение сессии этого потребителя
        # и только тогда ре-балансирует
        consumer.close()


dlq_prod = create_producer(bootstrap_servers, dlq_topic)
consume(bootstrap_servers, consumers_group_id_1, topic_1, dlq_prod)
