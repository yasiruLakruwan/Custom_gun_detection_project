import os
from setuptools import setup,find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()


setup(
    name="Custom gun detection project",
    version="0.1",
    author="Yasiru Lakruwan",
    packages=find_packages(),
    install_requires=requirements
)


# Setup file