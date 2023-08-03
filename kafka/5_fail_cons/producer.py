import json
import socket
import time

from confluent_kafka import Producer

from config import topic_2, bootstrap_servers, topic_1


def delivery_report(err, msg):
    """ Отчет по доставке сообщений """
    if err:
        print(f'Сообщение доставлено с ошибкой: {err}')
    else:
        print(f'Сообщение доставлено в топик {msg.topic()} [{msg.partition()}] со сдвигом {msg.offset()}')


def kafka_producer_example(bootstrap_servers, topic):
    # Producer конфигурация
    # Смотри подробно расписанную тут - https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {
        # Mandatory
        'bootstrap.servers': bootstrap_servers,
        'client.id': socket.gethostname(),
        # Optional
    }
    producer: Producer = Producer(**conf)

    # Имитация отправки сообщений
    for i in range(1000):
        try:
            message_value = f'Сообщение {i}'
            # Асинхронная доставка сообщений(следуя документации)
            # Можем указать: топик, ключ, партицию и callback функцию
            producer.produce(
                topic,
                value=message_value.encode('utf-8'),
                callback=delivery_report
            )
            time.sleep(1)
        except BufferError:
            print(f'Очередь продюсера(приложения) уже заполнена ({len(producer)} сообщений ожидают отправки)')
        except Exception as ex:
            raise ex
        finally:
            # Todo
            producer.poll(5)

    # Ожидание, пока все сообщения отправятся
    # Note 1: Следует вызывать перед закрытием производителя,
    # чтобы гарантировать доставку всех ожидающих/поставленных в очередь/находящихся сообщений.
    # Note 2: не использовать вместо poll()
    # Note 3: Вызывает poll() пока в локальном буфере producer не останется сообщений на отправку
    producer.flush()


kafka_producer_example(bootstrap_servers, topic_1)
