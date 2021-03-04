# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from time import sleep
from datetime import datetime
from {{cookiecutter.name}} import config
from {{cookiecutter.name}}.processing import DataProcessor
{% if cookiecutter.flow_consumer == "yes" %}from {{cookiecutter.name}}.kafka import KafkaConsumer{%- endif %}
{% if cookiecutter.flow_producer == "yes" %}from {{cookiecutter.name}}.kafka import KafkaProducer{%- endif %}


procesor = DataProcessor()
{% if cookiecutter.flow_consumer == "yes" %}consumer = KafkaConsumer(config.KAFKA_INPUT_TOPICS, config.KAFKA_CONSUMER_SETTINGS){%- endif %}
{% if cookiecutter.flow_producer == "yes" %}producer = KafkaProducer(config.KAFKA_OUTPUT_TOPICS, config.KAFKA_PRODUCER_SETTINGS){%- endif %}


def behaviour():

	# read or generate data
	{% if cookiecutter.flow_consumer == "yes" %}data = consumer.consume(){% else %}data = [{'msg': datetime.now().isoformat()}]{%- endif %}
	{% if cookiecutter.flow_consumer == "no" %}sleep(1){%- endif %}

	# manage data
	processed = []
	for d in data:
		if d is not None:
			p = procesor.process(d['msg'])
			processed.append(p)
	
	{% if cookiecutter.flow_producer == "yes" %}
	# send or manage data
	for p in processed:
		producer.produce(p)
	{%- endif %}


def run():
	while True:
		behaviour()

if __name__ == '__main__':
	run()