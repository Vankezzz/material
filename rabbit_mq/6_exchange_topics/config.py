ampq_url = 'amqp://guest:guest@82.199.101.51:18479'
exchange = 'exchange_topics_exchange'

routing_keys = ["user.profile.created", "user.profile.verified", "user.profile.deleted","user.msg.deleted"]

binding_key_1 = "user.#"
binding_key_2 = "user.*.created"
binding_key_3 = "user.*.deleted"
