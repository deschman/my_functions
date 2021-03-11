# -*- coding: utf-8 -*-
"""Set up my_functions package."""


# %% Imports
import setuptools


# %% Script
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()
short_description = long_description[long_description.find('Description'):
                                     long_description.find('\n')]

setuptools.setup(
    name="my_functions", # Replace with your own username
    version="1.0.0",
    author="Dan Eschman",
    author_email="dan.eschman@gmail.com",
    description=short_description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deschman/my_functions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6")
