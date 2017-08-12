# Nested related entities filter for DRF OrderingFilter

A custom DRF OrderingFilter with support to nested related fields.

Still work in progress (a.k.a. "works for me")

## Build

`python setup.py bdist_wheel`

## Requirements

At the moment Django >= 1.10, DRF probably >= 3.x. Python 2.7 and 3.x (not tested yet).

## Installation

`pip install dist/djangorestframework_custom_filters_ordering-X.Y.Z-py2.py3-none-any.whl`

## Usage

Include in your `views.py` file. Don't forget to specify `ordering_fields`. See `tests/views.py`.

## Run tests

`python run_tests.py tests.test_serializers`

## Reference

[DRF issue on Github](https://github.com/encode/django-rest-framework/issues/1005)

Kudos to [rhunwicks](https://github.com/rhunwicks) and the other people in CC of that issue for the initial patch and following updates.

--> **PR and suggestions welcome!**
