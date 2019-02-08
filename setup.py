#!/usr/bin/python3
#setup
#by boot1110001

from distutils.core import setup

setup(
    # Application name:
    name="fastmind",

    # Version number (initial):
    version=open("version.txt").read().replace('\n',''),

    # Application author details:
    author="boot1110001",
    author_email="nothing@addr.ess",

    # Packages
    packages=[
        "bin",
        "bin.core",
        "bin.graphic"
    ],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/boot1110001/fastmind",

    #
    license="GPL v3.0",
    description="Solve mazes and measure your time to complete them as fast as you can.",

    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pygame"
    ],
)
