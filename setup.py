# future imports
from __future__ import unicode_literals

# stdlib imports
import re
from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-Jingle',
    version=get_version('mopidy_jingle/__init__.py'),
    url='https://github.com/ablanchard/mopidy-jingle',
    license='Apache License, Version 2.0',
    author='Alexandre Blanchard',
    description='Mopidy extension that plays jingle between tracks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Mopidy >= 3.0.0',
        'Pykka >= 1.1',
    ],
    entry_points={
        'mopidy.ext': [
            'jingle= mopidy_jingle:Extension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
