# Copyright {% now 'local', '%Y' %} {{ cookiecutter.author }}
# See LICENSE for details.


class DataProcessor:

	def process(self, data):
		print(f'processing in {{ cookiecutter.name }}: {data}')
		data = f'{data} -> {{ cookiecutter.name }}'

		return data