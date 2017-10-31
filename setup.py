"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/dvilela/wait_response
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wait_response',
    version='1.0.0',

    description='Wait for some http response',
    long_description=long_description,

    url='https://github.com/dvilela/wait_response',

    author='dvilela',
    author_email='denisxvilela@gmail.com',

    license='MIT',

    keywords='http response wait-for wait functional test',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],

    install_requires=['requests'],

    entry_points={
        'console_scripts': [
            'wait_response=wait_response:main',
        ]
    }
)
