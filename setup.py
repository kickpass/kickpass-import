#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(name='kickpass-import',
      version='0.0.0',
      description='Import password from various password manager into kickpass',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/kickpass-import',
      packages=find_packages(),
      scripts=['scripts/kickpass-import'],
      install_requires=['kickpass','lxml'],
      test_suite="tests",
      classifiers=['Environment :: Console',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
