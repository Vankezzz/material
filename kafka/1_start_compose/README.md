# Описание
Данный docker compose включает в себя последнюю версию `kafka+KRaft` (вместо `zookeeper`, но его надо включить) и `kafka-ui`

## Запуск примера
1. Заменить `yuor host` 
в `KAFKA_ADVERTISED_LISTENERS: 'PLAINTEXT://broker:29092,PLAINTEXT_HOST://<your_host>:9092'`
на ваш ip адресс откуда вы будете к нему обращаться
2. ввести команду в терминале 
```shell
docker compose up --build
```
3. Убедится, что запущен `kafka-ui` на порту 8080 вашей машины