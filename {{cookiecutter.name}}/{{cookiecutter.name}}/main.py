
from {{cookiecutter.name}} import config
from {{cookiecutter.name}}.processing import DataProcessor
{% if cookiecutter.flow_consumer == "yes" %}from {{cookiecutter.name}}.kafka import KafkaConsumer{%- endif %}
{% if cookiecutter.flow_producer == "yes" %}from {{cookiecutter.name}}.kafka import KafkaProducer{%- endif %}


{% if cookiecutter.flow_consumer == "yes" %}consumer = KafkaConsumer(config.KAFKA_INPUT_TOPICS, config.KAFKA_CONSUMER_SETTINGS){% else %}generator = DataProcessor(){%- endif %}
procesor = DataProcessor()
{% if cookiecutter.flow_producer == "yes" %}producer = KafkaProducer(config.KAFKA_OUTPUT_TOPICS, config.KAFKA_PRODUCER_SETTINGS){% else %}handler = DataProcessor(){%- endif %}


def behaviour():

	# read or generate data
	{% if cookiecutter.flow_consumer == "yes" %}data = consumer.consume(){% else %}data = generator.process(){%- endif %}

	# manage data
	processed = []
	for d in data:
		if d is not None:
			p = procesor.process(d['msg'])
			processed.append(p)

	# send or manage data
	for d in processed:
		{% if cookiecutter.flow_producer == "yes" %}producer.produce(processed)	{% else %}manager.process(processed){%- endif %}


def run():
	while True:
		behaviour()

if __name__ == '__main__':
	run()