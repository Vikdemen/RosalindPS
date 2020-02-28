#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='RosalindProblemSolver',
    version='0.0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    url='https://github.com/Vikdemen/RosalindPS',
    license='MIT License',
    author='Demenev Viktor',
    author_email='viktor.demen@gmail.com',
    description='Rosalind problem solver',
    entry_points={
        'console_scripts': ['rosalind-ps = rps.__main__:main']
    }
)
