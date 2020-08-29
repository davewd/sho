#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
"pip==20.2.2",
"bump2version==1.0.0",
"llvmlite==0.34.0",
"wheel==0.35.1",
"watchdog==0.10.2",
"flake8==3.8.1",
"ipython==7.16.0",
"tox==3.19.0",
"coverage==5.1",
"Sphinx==3.2.1",
"twine==3.1.1",
"pandas==1.1.1",
"numpy==1.19.1",
"pivottablejs==0.9.0",
"pandas_profiling==2.8.0",
"seaborn==0.10.1",
"pytest==6.0.1",
"pytest-runner==5.2"
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['unittest>=3', ]

setup(
    author="David Dawson",
    author_email='davedawson.co@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Visualize python objects in the best way possible",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sho',
    name='sho',
    packages=find_packages(include=['sho', 'sho.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/davewd/sho',
    version='0.4.23',
    zip_safe=False,
)
