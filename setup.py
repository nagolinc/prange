#!/usr/bin/env python

from distutils.core import setup
import glob

os.chdir("src")
data_files=glob.glob('prange/data/*.txt')


print data_files

setup(name='prange',
      version='0.1',
      description='A Complex Python Progress Meter',
      author='Logan Zoellner',
      author_email='nagolinc@gmail.com',
      url='https://github.com/nagolinc/prange',
      
      packages=['prange'],
      package_dir={'prange': 'src/prange'},
      data_files=[('prange/data',data_files)]
     )
