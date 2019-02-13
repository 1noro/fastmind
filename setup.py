#!/usr/bin/python3
#setup
#by boot1110001

from setuptools import setup, find_packages

setup(
    # Application name:
    name="fastmind",

    # Version number (initial):
    version=open("version.txt").read().replace('\n',''),

    # Application author details:
    author="boot1110001",
    author_email="nothing@addr.ess",
    keywords="solve-mazes game libre-software mazes labyrinth labyrinth-game 2d-game minimalist pygame",

    # Packages
    packages=find_packages(),

    python_requires=">=3.5",

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="https://github.com/boot1110001/fastmind",
    license="GPL v3.0",
    description="Solve mazes and measure your time to complete them as fast as you can.",
    long_description=open("README.md").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pygame"
    ],

    data_files=[
        ('', [
            'fastmind.py',
            'version.txt'
        ]),
        ('lvls', [
            'lvls/0.lv',
            'lvls/1.lv',
            'lvls/2.lv',
            'lvls/3.lv',
            'lvls/4.lv'
        ]),
        ('media', [
            'media/icon.ico',
            'media/node.ttf'
        ])
    ],

    entry_points={  # Optional
        "console_scripts": [
            # 'sample=sample:main',
            "fastmind=core:main"
        ]
    },

    # scripts=["fastmind.py"],

    project_urls={  # Optional
        "Source": "https://github.com/boot1110001/fastmind"
    }
)
