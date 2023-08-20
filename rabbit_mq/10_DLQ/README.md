# Описание
Пример демонстрирует работу DLQ с ошибкой в схеме типа work queues.

Сам consumer моделирует задержку в 2 секунды - это нужно, 
чтобы показать как сообщения с 10 приоритетом обрабатываются в первую очередь.

> При обьявлении queue нужно указать exchange и queue - DLQ работает по принципу Direct
```
result = channel.queue_declare(
    queue=queue_1,
    arguments={
        'x-message-ttl': 1000,
        "x-dead-letter-exchange": dlq_exchange,
        "x-dead-letter-routing-key": dlq_routing_key
    }
)
```

> consumer_1 и consumer_2 обслуживают одну очередь, 
> однако consumer_1 каждое 3 сообщение будет отсылать в dlq ошибку. Обязательно должно быть `requeue=False`, 
> иначе сообщения будут снова доставлены в ту же очередь и обработаны
```
if method.delivery_tag % 3 == 0:
    print("Отправляем сообщение в DLQ")
    # ch.basic_nack(delivery_tag=method.delivery_tag,requeue=False)
    ch.basic_reject(delivery_tag=method.delivery_tag,requeue=False)
else:
    ch.basic_ack(delivery_tag=method.delivery_tag)
```

## Запуск примера
1. Запустить экземпляр consumer_1
```shell
python.exe consumer.py
```
2. Запустить экземпляр consumer_2
```shell
python.exe consumer_2.py
```
3. Запустить экземпляр consumer_dlq
```shell
python.exe consumer_dlq.py
```
4. Запустить producer
```shell
python.exe producer.py
```
5. Наблюдать как сообщения из очереди попадают в DLQ