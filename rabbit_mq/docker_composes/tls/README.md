1. Для сервера указать hostname
2. Нужно сгенерировать самоподписанный сертификат с помощью `tls-gen`
```bash
git clone https://github.com/rabbitmq/tls-gen tls-gen
cd tls-gen/basic
# секрет для сертификата, можем не указывать
make PASSWORD=bunnies
make verify
make info
ls -l ./result
```
3. У нас в `tls-gen` появилась папка `basic`, где и лежит папочка с сертификатами `result`
4. Так как имена сертификатов строятся в зависимости от хоста, 
то желательно переименовать их в следующем виде:
```
ca_certificate.pem
ca_key.pem

client_certificate.pem
client_key.pem

server_certificate.pem
server_key.pem
```
4. Положить все сертификаты в папку `certs` и разместить рядом с `docker-compose.tls.yml` в соответствии с volumes
```
- "./certs/ca_certificate.pem:/etc/ssl/ca_certificate.pem:ro"
- "./certs/server_certificate.pem:/etc/ssl/server_certificate.pem:ro"
- "./certs/server_key.pem:/etc/ssl/server_key.pem:ro"
```
5. Убедиться, что также в `rabbitmq.conf` все пути указаны верно, и особенно верен `ssl_options.password`
6. Запустить `docker-compose.tls.yml`