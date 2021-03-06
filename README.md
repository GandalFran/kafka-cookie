# Kafka subsystem as Python Package Cookie

<div align="center">
  <img src="https://github.com/GandalFran/kafka-cookie/blob/main/logo.png" height="300px" hspace="20">
</div>

## Installation
1. install [cookiecutter](https://github.com/cookiecutter/cookiecutter) with `pip3 install cookiecutter`
2. run template generation with `cookiecutter https://github.com/GandalFran/kafka-cookie.git`
3. fill properties as following
```
author [Franz Kafka]: Author
email [franz@kafka.com]: email@email.ml
name [the_metamorphosis]: my_project
kafka_num_tries [10]: 3
kafka_input_topics [input-topic]: topic1,topic2,topic3
kafka_output_topics [output-topic]: topic4
kafka_group_id [package_group_id]: my_group
kafka_broker [localhost:9092]: myserver.com:9092
kafka_delivery_timeout [3000]: 10000
flow_producer [yes]: yes
flow_consumer [yes]: no
```
