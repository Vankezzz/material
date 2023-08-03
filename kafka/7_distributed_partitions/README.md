# Описание
Данный пример демонстрирует как идет балансировка по хешу (по key у message), в других же случаях round-robin
> Порядок записей сохраняется относительно партиции, а не топика
## Дополнительная информация
в producer.py есть uuid.uuid1(), который будет уникальным ключом операции
```shell
producer.produce(
                topic,
                key=str(uuid.uuid1()),
                value=message_value.encode('utf-8'),
                callback=delivery_report
            )
```
## Запуск примера
1. Запустить 3 consumer в разных терминалах 
> сначала посмотреть насколько партиций он подпишется, а потом запускать другой
```shell
python.exe consumer.py
```
2. Запустить producer
```shell
python.exe producer.py
```
3. Наблюдать как в каждом consumer будет более равномерно распределяться отправка сообщений