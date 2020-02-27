from setuptools import setup

setup(
    name='rosalind-ps',
    version='0.0.1',
    packages=['rps'],
    package_dir={'': 'src'},
    python_requires='>=3.7',
    url='https://github.com/Vikdemen/RosalindPS',
    license='MIT License',
    author='vikdemen',
    author_email='viktor.demen@gmail.com',
    description='A simple tool for solving Rosalind problems',
    classifiers=['Programming Language :: Python :: 3'],
    keywords='bioinformatics practice', install_requires=['pytest']
)



