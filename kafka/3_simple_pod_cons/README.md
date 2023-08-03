# Описание
Данный пример демонстрирует простую связь 1 producer -> topic с 1 партицией -> 1 consumer
## Дополнительно

Подписаться можно по паттерну: 
`consumer.subscribe(["^my_topic.*", "^another[0-9]-?[a-z]+$"])`

## Запуск примера
1. Запустить consumer в одном терминале 
```shell
python.exe consumer.py
```
> Мы должны убедится в назначении партиции 
```
Назначили партиции: [TopicPartition{topic=topic2,partition=%I32d,offset=%s,leader_epoch=%s,error=%s}]
```
2. Запустить producer в одном терминале 
```shell
python.exe producer.py
```
3. Смотреть в consumer
```
Сообщение доставлено в топик topic2 [0] со сдвигом 0
Сообщение доставлено в топик topic2 [0] со сдвигом 1
Сообщение доставлено в топик topic2 [0] со сдвигом 2
```
4. Убедится, что сообщения появились в `kafka-ui` в topic2
