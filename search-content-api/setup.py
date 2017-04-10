from distutils.core import setup
setup(
    name = 'search-content-api',
    packages = ['search-content-api'],
    version = '1.0.1',
    description = 'A university project to create index and search for result from a given dataset from a given string',
    author = 'Vu Thanh Tam',
    author_email = 'vuthanhtam1506@gmail.com',
	data_files = [('/data/data.txt',['data-file'])],
	classifiers = [ 
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
	'Intended Audience :: Education',
	'Development Status :: 1 - Planning',
	'Natural Language :: Vietnamese',
	'Topic :: Database :: Database Engines/Servers'
	]
)