#!/usr/bin/python3
#setup
#by boot1110001

from distutils.core import setup

setup(
    # Application name:
    name="fastmind",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="boot1110001",
    author_email="notthing@addr.ess",

    # Packages
    packages=["bin"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://null.null",

    #
    license="LICENSE",
    description="Solve mazes and measure your time to complete them as fast as you can.",

    long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pygame",
    ],
)
