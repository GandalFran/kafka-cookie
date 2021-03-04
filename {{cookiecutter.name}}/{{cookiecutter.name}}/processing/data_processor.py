# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from time import sleep
from datetime import datetime

class DataProcessor:

	def process(self, data=None):
		if data is None:
			sleep(1)
			data = datetime.now().isoformat()

		print(f'processing in {{ cookiecutter.name }}: {data}')
		return data