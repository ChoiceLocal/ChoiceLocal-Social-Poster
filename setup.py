try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ChoiceLocal-Social-Poster',
    'author': 'ChoiceLocal',
    'url': 'github?',
    'download_url': '...github also?',
    'author_email': 'adarling@choicelocalmarketing; mshaw@choicelocalmarketing.com',
    'version': '0.1',
    'install_requires': ['requests, openpyxl, simplejson, google-api-python-client'],
    'packages': ['MAIN'],
    'scripts': [],
    'name': 'ChoiceLocal-Social-Poster'
}

setup(**config)