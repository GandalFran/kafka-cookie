# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.

from datetime import datetime

class DataProcessor:

	def process(self, data=None):
		if data is None:
			data = datetime.now().isoformat()

		print(f'processing in {{ cookiecutter.name }}: {data}')
		return data