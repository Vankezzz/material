from asyncio import Future
from typing import Dict
from confluent_kafka.admin import AdminClient, NewTopic
from config import cluster_bootstrap_servers, dlq_topic

admin: AdminClient = AdminClient({'bootstrap.servers': cluster_bootstrap_servers})

# Note: В продакшен среде лучше ставить replication_factor=3 для durability
dlq_topic = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in [dlq_topic]]

# Создание topics асинхронно
new_topics_fs: Dict[str, Future] = admin.create_topics(dlq_topic)

# Ожидаем создание topics
for topic, future in new_topics_fs.items():
    try:
        future.result()  # The result itself is None
        print("Топик {} создан".format(topic))
    except Exception as e:
        print(f"Ошибка при создании topic {topic}: {e}")
