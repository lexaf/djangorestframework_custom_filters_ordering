#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()


with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
        link.startswith('-f')]


setup(
    name='djangorestframework-custom-filters-ordering',
    version='0.0.1',
    packages=find_packages(),
    install_requires=libraries,
    dependency_links=dependency_links,
    long_description=long_description,
    # include_package_data=True,
    test_suite='tests',
    author='apiraino@github',
    author_email='apiraino@github',
    maintainer='apiraino@github',
    maintainer_email='apiraino@github',
    description='Custom Django REST Framework filters with support of related entity ordering',
    keywords=['django', 'REST', 'rest_framework', 'filters'],
    url='https://github.com/apiraino/djangorestframework_custom_filters_ordering'
)
