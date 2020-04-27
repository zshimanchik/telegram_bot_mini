#!/usr/bin/env python

from distutils.core import setup

with open('requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file if line.strip()]

with open('readme.md') as f:
    long_description = f.read()

setup(
    name='telegram_bot_mini',
    version='1.1.0',
    description='Mini library to work with telegram bot api',
    long_description=long_description,
    keywords='telegram bot api sdk',
    author='Zakhar Shymanchyk',
    author_email='zakshyman@gmail.com',
    install_requires=requirements,
    # url='https://www.python.org/sigs/distutils-sig/',
    packages=['telegram_bot_mini'],
 )
