from setuptools import setup

setup(
    name='RosalindProblemSolver',
    version='0.0.1',
    packages=['rps', 'rps.heredity_problems', 'rps.sequence_problems', 'rps.dynamic_programming_problems'],
    package_dir={'': 'src'},
    url='https://github.com/Vikdemen/RosalindPS',
    license='MIT License',
    author='Demenev Viktor',
    author_email='viktor.demen@gmail.com',
    description='Rosalind problem solver', install_requires=['pytest']
)
