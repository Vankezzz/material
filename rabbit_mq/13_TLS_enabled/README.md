# Описание
Пример демонстрирует подключение по tls для consumer и producer, также создается durable queue

> Обратить внимание на utils.py, где у нас создается подключение. 
> 
> Сами сертификаты можно получить из примера docker_composes/tls, 
> после генерации сертификатов для сервера и клиента
> 
> При появлении ошибок можно попробовать проверить сертификаты 
> на правильность создания [тут](https://www.rabbitmq.com/troubleshooting-ssl.html)
>
> Еще может быть причиной плохого подключения firewall
> (тут прям лучше сразу выключить, а потом после успешного развертывания включить)

## Запуск примера
1. Развернуть docker_compose с tls в docker_composes/tls
2. Не забыть переместить клиентские и CA сертификаты в проект,
а после указать пути до них в config
3. Запустить consumer
```shell
python.exe consumer.py
```
4. Посмотреть в UI в connections как появится у подключения галочка TLS
5. Запустить producer и удостовериться, что все работает
```shell
python.exe producer.py
```