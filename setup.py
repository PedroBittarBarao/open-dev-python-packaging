#!/usr/bin/env python3
from setuptools import setup

setup(name='dev_aberto',
      version='0.3.4',
      packages=['dev_aberto'],
      scripts=['scripts/hello.py'],
      python_requires='>=3.12',
      install_requires=['requests', 'setuptools','wheel'],
      )