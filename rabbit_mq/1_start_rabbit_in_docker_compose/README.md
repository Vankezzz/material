1. Переменные окружения для [docker-compose](https://www.rabbitmq.com/configure.html#supported-environment-variables). Полезные переменные:
```
RABBITMQ_SERVER_ADDITIONAL_ERL_ARGS= -rabbit
disk_free_limit 2147483648 # Если на сервере остается менее 2гб, то переходит в режим "защиты" и перестает писать в стейт (по умолчанию 48 мб значение, но чаще всего из-за этого может полностью сломаться стейт - советы ПРО)
```
2. Образы с префиксом `-management` открывают доступ к UI менеджеру на порту 15672 с логином и паролем guest/guest
3. Добавление плагинов к rabbit делается через создание Dockerfile:
```dockerfile
FROM rabbitmq:3.12-management
RUN rabbitmq-plugins enable --offline rabbitmq_mqtt rabbitmq_federation_management rabbitmq_stomp
```
4. Настраивать rabbit можно через конфигурацию внутри контейнера `/etc/rabbitmq/rabbitmq.conf`. Вся доступная конфигурация хранится [тут](https://www.rabbitmq.com/configure.html#configuration-files)
5. docker compose down -v --remove-orphans && docker volume prune -f && docker compose up --build --force-recreate

# Статьи
1. [Управление UI](https://habr.com/ru/companies/southbridge/articles/704208/)