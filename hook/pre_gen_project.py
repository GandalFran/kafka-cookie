import sys

name = '{{ cookiecutter.name }}'
banned_characters = [' ', '\n', '\t', '-']
for c in banned_characters:
	if c in name:
		print(f'ERROR: the package name ({name}) can\'t contain the character ({c})')
		sys.exit(1)