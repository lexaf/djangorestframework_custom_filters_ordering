#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='djangorestframework-custom-filters-ordering',
    version='0.0.1',
    packages=find_packages(exclude='tests'),
    description='Custom Django REST Framework filters with support of related entity ordering',
    long_description="Custom Django REST Framework filters with support of related entity ordering",
    include_package_data=True,
    test_suite='tests',
    author='apiraino@github',
    maintainer='apiraino@github',
    keywords=['django', 'REST', 'rest_framework', 'filters'],
    url='https://github.com/apiraino/djangorestframework_custom_filters_ordering',
    download_url='https://pypi.python.org/pypi/djangorestframework-custom-filters-ordering',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ]

)
