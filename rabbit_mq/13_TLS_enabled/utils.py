import ssl
import pika
from pika import ConnectionParameters


def create_tls_connection_params(
        host: str,
        tls_port: int,
        user: str,
        password: str,
        ca_cert_path:str,
        client_cert_path:str,
        client_key_path:str,
        secret: str = None
) -> ConnectionParameters:

    context = ssl.create_default_context(
        cafile=ca_cert_path,
    )
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_cert_chain(client_cert_path,
                            client_key_path,
                            password=secret)
    credentials = pika.PlainCredentials(user, password)
    ssl_options = pika.SSLOptions(context, host)
    conn_params: ConnectionParameters = pika.ConnectionParameters(
        host=host,
        port=tls_port,
        ssl_options=ssl_options,
        credentials=credentials
    )
    return conn_params
