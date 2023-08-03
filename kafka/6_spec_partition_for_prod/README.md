# Описание
Данный пример демонстрирует как можно отсылать данные определенной партиции. Это нужно, к примеру, 
если мы масштабируем какой-нибудь сервис финансов и 1 consumer привязаны определенные пользователи
> Порядок записей сохраняется относительно партиции, а не топика
## Дополнительная информация
в producer.py есть тернарная конструкция, которая по очереди будет слать в каждую партицию по 5 сообщений
```shell
producer.produce(
                topic,
                partition=0 if i % 15 < 5 else 1 if 5 <= i % 15 < 10 else 2,
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
3. Наблюдать как в каждом consumer будет по 5 сообщений