from setuptools import setup

setup(
	name='utlyz',
	version=1.0,
	py_modules=[
		'fbcli',
		'cricbuzz',
		'lyrics',
		'searching',
		'news',
		'football',
		'xkcd',
	],
	install_requires=[
		'click',
		'bs4',
		'BeautifulSoup',
		'mechanize',
		'requests',
		'google',
		'wikipedia',
	],
	entry_points={
		'console_scripts':[
		'fbcli=fbcli:cli',
		'cricbuzz=cricbuzz:cli',
		'lyrics=lyrics:cli',
		'searching=searching:cli',
		'news=news:cli',
		'football=football:cli',
		'xkcd=xkcd:cli',
		]
	},
)
