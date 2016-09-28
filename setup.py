#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from setuptools import setup, find_packages

setup(
    name='pylint-comma',
    version='0.0.1',
    url='https://github.com/taozle/pylint-comma',
    author='taozle',
    author_email='zhangliyang26@gmail.com',
    description='Detect unexpected comma',
    packages=find_packages(),
    install_requires=[
        'pylint',
    ],
    license='GPLv2',
    keywords='pylint comma plugin'
)
