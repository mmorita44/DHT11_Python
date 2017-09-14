#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='check dht11',
    version='1.0.1',
    description='Check digital temperature and humidity data from the DHT11.',
    url='https://github.com/mmorita44/DHT11_Python',
    author='Masato Morita',
    author_email='m.morita44@hotmail.com',
    license='MIT',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Customer Service',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4'],
    scripts=['scripts/check-dht11'],
    packages=find_packages(),
    install_requires=['requests', 'RPi.GPIO']
)
