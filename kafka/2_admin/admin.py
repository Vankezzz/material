from asyncio import Future
from typing import Dict
from confluent_kafka.admin import AdminClient
from kafka.admin import NewTopic

from config import cluster_bootstrap_servers, topic_2, topic_1

admin: AdminClient = AdminClient({'bootstrap.servers': cluster_bootstrap_servers})

# Note: В продакшен среде лучше ставить replication_factor=3 для durability
new_topics_3part = [NewTopic(topic, num_partitions=3, replication_factor=1) for topic in [topic_1]]
new_topics_1part = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in [topic_2]]

# Создание topics асинхронно
new_topics_fs: Dict[str, Future] = admin.create_topics([*new_topics_3part,*new_topics_1part])

# Ожидаем создание topics
for topic, future in new_topics_fs.items():
    try:
        future.result()  # The result itself is None
        print("Топик {} создан".format(topic))
    except Exception as e:
        print(f"Ошибка при создании topic {topic}: {e}")
