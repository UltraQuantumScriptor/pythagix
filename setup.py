# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pythagix",
    version="0.2.14",
    author="UltraQuantumScriptor",
    description="Pythagix is a lightweight Python library that provides a collection of mathematical utility functions for number theory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
