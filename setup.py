#!/usr/bin/env python

from distutils.core import setup

data_files=glob.glob('data/*.txt')

setup(name='prange',
      version='0.1',
      description='A Complex Python Progress Meter',
      author='Logan Zoellner',
      author_email='nagolinc@gmail.com',
      url='https://github.com/nagolinc/prange',
      py_modules=['prange'],
      data_files=[('data',data_files)]
     )
