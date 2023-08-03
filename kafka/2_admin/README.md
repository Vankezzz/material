# Описание
Данный пример демонстрирует управление конфигурацией топиков кафки через AdminClient

## Запуск примера
1. ввести команду в терминале 
```shell
python.exe admin.py
```
2. Убедится, что созданы с помощью `kafka-ui`

## Где можно применить?
1. Динамическая инициализация новых топиков с партициями и количеством репликаций
```python
from confluent_kafka.admin import  NewTopic
NewTopic("topic", num_partitions=3, replication_factor=1)
```
2. Получение всех топиков (допустим для проверка на существование топика)
```python
from confluent_kafka.admin import  AdminClient
admin: AdminClient = AdminClient({'bootstrap.servers': "your_address"})
admin.list_topics()
```
3. Удаление топиков
```python
from confluent_kafka.admin import  AdminClient
admin: AdminClient = AdminClient({'bootstrap.servers': "your_address"})
admin.delete_topics(["topic1","topic2"])
```
4. Управление конфигурацией Kafka - [тут прям много примеров](https://github.com/confluentinc/confluent-kafka-python/blob/master/examples/adminapi.py)