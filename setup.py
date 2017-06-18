#!/usr/bin/env python

from distutils.core import setup
import glob

setup(name='prange',
      version='0.1',
      description='A Complex Python Progress Meter',
      author='Logan Zoellner',
      author_email='nagolinc@gmail.com',
      url='https://github.com/nagolinc/prange',
      
      packages=['prange'],
      package_dir={'prange': 'src/prange'},
      package_data={  'prange': ['data/*.txt']}
      
     )
