ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = '5_exchange_topics'
queue_1 = 'consumer_group_1'
queue_2 = 'consumer_group_2'
routing_keys = ["user.profile.created", "user.profile.verified", "user.profile.deleted"]

binding_key_1 = "user.#"
binding_key_2 = "user.*.created"
binding_key_3 = "user.*.deleted"
