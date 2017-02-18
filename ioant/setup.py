from setuptools import setup, find_packages
import os
import sys


setup(
    name="ioant",
    version="0.1.5",
    packages=find_packages(),
    include_package_data=True,
    author="Adam Saxen",
    author_email="adam@asaxen.com",
    description="This package is used for python scripts in IOAnt platform solution",
    license="MIT",
    keywords="",
    url="http://ioant.com",   # project home page, if any
    install_requires=[
        "nose>=1.3.7",
    ],

)
