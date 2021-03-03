# Kafka subsystem as Python Package Cookie

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/Kafka_portrait.jpg" height="300px" hspace="20">
</div>

## Installation
1. install [cookiecutter](https://github.com/cookiecutter/cookiecutter) with `pip3 install cookiecutter`
2. run template generation with `cookiecutter https://github.com/GandalFran/kafka-cookie.git`
3. fill properties as following
```
author [Author]: Franz Kafka
email [example@example.example]: franz@kafka.com
name [kafka-cookie-generated-package]: The Metamorphosis
kafka.num_tries [10]: 3
Select kafka.input_topics:
1 - input-topic
Choose from 1 [1]: 1
Select kafka.output_topics:
1 - output-topic
Choose from 1 [1]: 1
kafka.group_id [package_group_id]: group_id
kafka.broker [localhost:9092]:
kafka.delivery_timeout [3000]:
flow.producer [yes]: yes
flow.consumer [yes]: yes
```
