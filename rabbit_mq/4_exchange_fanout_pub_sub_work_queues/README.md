# Описание
Данный пример демонстрирует архитектуру fanout с двумя work_queues
> Аналог логики подключения consumer groups в Kafka

## Запуск примера
1. Запустить consumer_1 в одном терминале в двух экземплярах и убедиться в том, 
что они привязаны к одному queue_1 с разными идентификаторами (consumer_tag)
```shell
python.exe consumer.py
```
2. Запустить consumer_2 в одном терминале в двух экземплярах и убедиться в том, 
что они привязаны к одному queue_2 с разными идентификаторами (consumer_tag)
```shell
python.exe consumer_2.py
```
3. Убедиться в UI, что схема работает ("Queues and Streams"). 
Мы должны увидеть как у каждой очереди с именами consumer_group_1 и consumer_group_2 есть по 2 потребителя
4. Запустить producer и наблюдать как сообщения равномерно распределяются между consumer_groups равномерно
```shell
python.exe producer.py
```