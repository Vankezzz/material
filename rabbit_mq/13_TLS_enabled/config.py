ampq_url = 'amqp://guest:guest@almaz.loc:5672'
host = "almaz.loc"
tls_port = "5671"
user = 'guest'
password = 'guest'
secret = 'bunnies'

ca_cert_path = "../certs/ca_certificate.pem"
client_cert_path = "../certs/client_certificate.pem"
client_key_path = "../certs/client_key.pem"

exchange = '13_TLS_enabled'
queue = 'tls_queue'
