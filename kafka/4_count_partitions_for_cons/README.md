# Описание
Данный пример демонстрирует:
1. Если consumers больше, чем partitions, то будет простой какого-нибудь consumer
2. Если consumers меньше, чем partitions, то при масштабировании consumer он просто возьмет 
себе нужную partition и разгрузит другого

## Запуск примера
1. Запустить 3 consumer в разных терминалах 
> сначала посмотреть насколько партиций он подпишется, а потом запускать другой
```shell
python.exe consumer.py
```
2. Запустить 4 consumer и убедиться, что 1 из consumer выдаст `Партиция простаивает`. Это происходит из-за того, что у нас 3 партиции, а consumers = 4