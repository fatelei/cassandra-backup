# -*- coding: utf8 -*-
"""cassandra_backup."""

from setuptools import setup

from cassandra_backup import __version__


setup(
    name="cassandra_backup",
    version=__version__,
    description="cassandra backup tools",
    install_requres=[
        "boto3==1.3.1"
    ],
    packages=["cassandra_backup"],
    zip_safe=False,
    url="https://github.com/fatelei/cassandra-backup",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries",
    ],
    license="BSD License"
)
