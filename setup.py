#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='encoding',
    version='0.1',
    author='DramaFever',
    url='https://github.com/djworth/python-encoding',
    packages=find_packages(),
    package_dir={'encoding': 'encoding'},
    install_requires=[
        'lxml',
    ],
)
