#!/usr/bin/env python


import os
import re
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open(os.path.join('sequtils', '__init__.py'), 'r') as fi:
    __version__ = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fi.read()).group(1)


with open('requirements.txt', 'r') as reqs:
    requirements = map(lambda x: x.rstrip(), reqs.readlines())


test_requirements = [
    'nose',
    'nose-parameterized'
]


with open('README.rst') as readme_file:
    readme = readme_file.read()


setup(
    name='sequtils',
    version=__version__,
    description="Python utilities for sequence comparison, quantification, and feature extraction.",
    long_description=readme,
    author="atgtag",
    author_email='atgtag@genova.io',
    url='https://github.com/atgtag/sequtils',
    package_dir={'sequtils': 'sequtils'},
    packages=['sequtils'],
    include_package_data=True,
    install_requires=requirements,
    license="Apache-2.0",
    zip_safe=False,
    keywords=['sequtils', 'seq', 'sequence', 'metrics', 'ngs', 'sequencing', 'distance', 'hamming', 'edit'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apple Public Source License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'sequtils = sequtils.__main__:main'
        ]
    },
)
