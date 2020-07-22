#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" setup.py for cookiecutter-fastapi."""

from setuptools import setup

__version__ = "0.2.0"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-fastapi",
    version=__version__,
    description="A Cookiecutter template for creating FastAPI projects quickly. Based on fork of https://github.com/arthurenrique/cookiecutter-fastapi",
    long_description=long_description,
    author="Thierry Bomandouki",
    author_email="engobi@gmail.com",
    url="https://github.com/engobi/cookiecutter-fastapi",
    download_url="",
    packages=[],
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Framework :: FastAPI",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development",
    ],
    keywords=(
        """
        cookiecutter, Python, projects, project templates, fastapi,
        skeleton, scaffolding, project directory, setup.py
        """
    ),
)
