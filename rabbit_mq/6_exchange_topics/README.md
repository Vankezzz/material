# Описание
Данный пример демонстрирует архитектуру topic доставки сообщения потребителю по routing_key. 
Каждая очередь имеет свой уникальный binding ключ (шаблон). 
Производитель отправляет сообщение с определенным routing_key **в определенный exchange**, 
потом берутся bindings всех очередей и как бы определяют **по шаблону** (потому что режим topic)
в какую очередь попадут сообщения

> Самое интересное лежит в config.py 
```
routing_keys = ["user.profile.created", "user.profile.verified", "user.profile.deleted","user.msg.deleted"]

binding_key_1 = "user.#"
binding_key_2 = "user.*.created"
binding_key_3 = "user.*.deleted"
```
> **routing_keys** - это ключи, с которыми может прийти сообщение
> 
> **binding_key_{номер очереди}** - это bindings определенных очередей. 
> Работают как шаблоны, где
> 
> **'*'** -  заменяет одно слово 
> 
> **'#'** -  экранирует все слова либо перед, либо после
> 
> Пример: приходит сообщение с routing_key=user.profile.created,
> тогда проверяется "в какую очередь оно попадет", 
> в нашем случае в очереди со следующими bindings: binding_key_1 и binding_key_2
## Запуск примера
1. Запустить consumer_1 в одном терминале и убедиться в том, 
что у него свой binding_key_1
```shell
python.exe consumer.py
```
2.  Запустить consumer_2 в одном терминале и убедиться в том, 
что у него свой binding_key_2
```shell
python.exe consumer_2.py
```
3. Запустить consumer_3 в одном терминале и убедиться в том, 
что у него свой binding_key_3
```shell
python.exe consumer_3.py
```

3. У producer появилась конструкция рандомного распределения сообщения по routing_key, 
которые заданы в виде шаблона в config файле
```
for i in range(100):
    routing_key = random.choice(routing_keys)
    message = f"Сообщение {i} отправлено по ключу {routing_key}"
```
4. Запустить producer и наблюдать как сообщения рандомно распределяются между очередями в зависимости от их binding
```shell
python.exe producer.py
```