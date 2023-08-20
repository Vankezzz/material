ampq_url = 'amqp://guest:guest@almaz.loc:5672'
exchange = '6_exchange_topics_exchange'

routing_keys = ["user.profile.created", "user.profile.verified", "user.profile.deleted","user.msg.deleted"]

binding_key_1 = "user.#"
binding_key_2 = "user.*.created"
binding_key_3 = "user.*.deleted"
