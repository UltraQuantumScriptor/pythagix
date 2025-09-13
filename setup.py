# -*- coding: utf-8 -*-
from setuptools import setup, find_packages, Extension

with open(
    "C:\\Users\\Sohaib\\Documents\\Nexus\\Code\\Python_work\\pythagix\\README.md",
    encoding="utf-8",
) as f:
    long_description = f.read()

numbering_extension = Extension(
    "pythagix.numbering",
    sources=["pythagix/numbering.c"],
)

prime_extension = Extension(
    "pythagix.prime",
    sources=["pythagix/prime.c"],
)

stat_extension = Extension(
    "pythagix.stat",
    sources=["pythagix/stat.c"],
)

ratio_extension = Extension(
    "pythagix.ratio",
    sources=["pythagix/ratio.c"],
)

setup(
    name="pythagix",
    version="0.2.22",
    author="UltraQuantumScriptor",
    description="Pythagix is a lightweight Python library that provides a collection of mathematical utility functions for number theory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    ext_modules=[numbering_extension, prime_extension, ratio_extension, stat_extension],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
