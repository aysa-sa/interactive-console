# Author: Alejandro M. BERNARDIS
# Email: alejandro.bernardis@gmail.com
# Created: 2019/11/22 14:13
# ~

from os import path
from io import open
from setuptools import setup, find_packages
from aysa.console import __version__ as console

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=console.__title__,
    version=console.__version__,
    description=console.__summary__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=console.__uri__,
    author=console.__author__,
    author_email=console.__email__,
    keywords='docker console services development deployment',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.6.*, <4',

    package_data={
        '': ['LICENSE', 'README.md']
    },

    install_requires=[
        
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],

    project_urls={
        'Bug Reports': console.__issues__,
        'Source': console.__uri__,
    },

)
