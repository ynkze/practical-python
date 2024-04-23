# script to package code - see setuptools guide to use

import setuptools

setuptools.setup(
    name="porty",
    version="0.0.1",
    author="ynkze",
    author_email="",
    description="Practical Python Code",
    packages=setuptools.find_packages()
)