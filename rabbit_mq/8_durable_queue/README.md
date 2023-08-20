# Описание
Пример демонстрирует durable для queue и exchange
> В producer при отправке сообщения дополнительно указывается флаг PERSISTENT_DELIVERY_MODE,
> что дает указание durable очереди записывать сообщение на жесткий диск (если не будет указан, 
> то мы потеряем все необработанные сообщения)
```
properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # сообщение в durable очереди запишется на диск
        )
```

> Назначение exchange и queue быть durable можно увидеть в consumer.py
```
channel.exchange_declare(
    exchange=exchange,
    durable=True
)
channel.queue_declare(
    queue=queue,
    durable=True
)
```
> Особенности:
> 1. Если durable будет только exchange, 
то при перезагрузке rabbitmq **наш exchange останется, а queue удалиться**
> 2. Если durable будет только queue, 
то при перезагрузке rabbitmq **наш queue останется и привяжется к default exchange, 
а наш exchange удалиться**
## Запуск примера
1. Запустить экземпляр consumer в разных терминалах и убедиться(в UI) в том, 
что он создал durable для exchange и queue
```shell
python.exe consumer.py
```
2. Запустить producer
```shell
python.exe producer.py
```
3. Отключить consumer, producer отправит пару сообщений в очередь
4. Остановить rabbitmq `docker stop rabbitmq` 
5. Перезапустить rabbitmq `docker start rabbitmq` 
6. Запустить экземпляр consumer и убедиться, 
что он получит те сообщения, которые были отправлены в пункте 3
```shell
python.exe consumer.py
```
### Примечание
Если в producer закомментируете строки с указанием сохранения сообщений на жестком диске
и повторите действия выше, то сообщения не сохранятся
```
properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE  # сообщение в durable очереди запишется на диск
        )
```