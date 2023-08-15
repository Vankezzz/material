import socket
import time
import uuid

from confluent_kafka import Producer

from config import topic_2, bootstrap_servers, topic_1, cluster_bootstrap_servers


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
        "acks": "all",
        'enable.idempotence': True,                 # Выключает дублирование сообщений
        'transactional.id': 'my-transactional-id',  # Уникальный Id для транзакции
    }
    producer: Producer = Producer(**conf)

    # Начало транзакции
    print("Инициализируем транзакцию")
    producer.init_transactions()
    try:
        print("Запускаем транзакцию")
        producer.begin_transaction()
        # Имитация отправки сообщений
        for i in range(5):
            # if i == 4:
            #     raise Exception("ломаем транзакцию")
            message_value = f'Сообщение {i}'
            # Асинхронная доставка сообщений(следуя документации)
            # Можем указать: топик, ключ, партицию и callback функцию
            producer.produce(
                topic,
                key=str(uuid.uuid1()),
                value=message_value.encode('utf-8'),
                callback=delivery_report
            )
            print(f"Добавили {message_value}")
            producer.poll(.5)
            time.sleep(1)
    except BufferError:
        print(f'Очередь продюсера(приложения) уже заполнена ({len(producer)} сообщений ожидают отправки)')
    except Exception as ex:
        producer.abort_transaction()
        raise ex
    finally:
        print(f"COMMIT транзакции")
        producer.commit_transaction()

    # Ожидание, пока все сообщения отправятся
    # Note 1: Следует вызывать перед закрытием производителя,
    # чтобы гарантировать доставку всех ожидающих/поставленных в очередь/находящихся сообщений.
    # Note 2: не использовать вместо poll()
    # Note 3: Вызывает poll() пока в локальном буфере producer не останется сообщений на отправку
    producer.flush()


kafka_producer_example(cluster_bootstrap_servers, topic_1)
