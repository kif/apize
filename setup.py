from setuptools import setup


setup(
	name = 'apize',
	version = '0.0.7',
	author = 'herrersystem',
	author_email = 'anton.millescamps@evhunter.fr',
	
	url = "http://github.com/herrersystem/apize",
	keywords = 'apize',
	description = 'Write quickly and easily to API clients',
	license = 'GPLv3',
	packages = ['apize'],
	install_requires = ['requests'],
	
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: GPL-3.0',
		'Topic :: Software Development',
		'Topic :: Software Development :: Libraries', 
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	],
)
