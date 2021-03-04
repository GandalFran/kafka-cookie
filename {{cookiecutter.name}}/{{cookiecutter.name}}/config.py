# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

# Kafka configuration
KAFKA_BROKER = "{{ cookiecutter.kafka_broker }}"

KAFKA_NUM_TRIES = {{ cookiecutter.kafka_num_tries }}
KAFKA_DELIVERY_TIMEOUT = {{ cookiecutter.kafka_delivery_timeout }}
KAFKA_INPUT_TOPICS = "{{ cookiecutter.kafka_input_topics }}".split(',')
KAFKA_PRODUCER_SETTINGS = {
    'retries': KAFKA_NUM_TRIES,
    'bootstrap.servers': KAFKA_BROKER,
    'default.topic.config': {
        'delivery.timeout.ms': KAFKA_DELIVERY_TIMEOUT
    }
}

KAFKA_GROUP_ID = "{{ cookiecutter.kafka_group_id }}"
KAFKA_OUTPUT_TOPICS = "{{ cookiecutter.kafka_output_topics }}".split(',')
KAFKA_CONSUMER_SETTINGS = {
    'group.id': KAFKA_GROUP_ID,
    'bootstrap.servers': KAFKA_BROKER,
    'default.topic.config': {
        'auto.offset.reset': 'earliest'
    }
}
