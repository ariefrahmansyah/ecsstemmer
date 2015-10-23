from setuptools import setup
setup(
	name='ecsstemmer',
	version='0.1',
	author='Arief Rahmansyah',
	author_email='ariefrahmansyah@hotmail.com',
	description='ECS Stemmer for Indonesian Language',
	py_modules=['ecsstemmer'],
	include_package_data = True,
    package_data = {
        '': ['rootwords.txt'],
        'static': ['rootwords.txt'],
    }
)