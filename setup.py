#!/usr/bin/python3
#setup
#by boot1110001

from distutils.core import setup

setup(
    # Application name:
    name="fastmind",

    # Version number (initial):
    version=open("fmind/version.txt").read().replace('\n',''),

    # Application author details:
    author="boot1110001",
    author_email="nothing@addr.ess",
    keywords="solve-mazes game libre-software mazes labyrinth labyrinth-game 2d-game minimalist pygame",

    # Packages
    packages=[
        "fmind",
        "fmind.core",
        "fmind.graphic",
        "fmind.graphic.elements",
        "fmind.languages"
    ],

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
        ('fmind', [
            'fmind/version.txt',
            'fmind/node.ttf',
            'fmind/icon.ico'
        ]),
        ('fmind/lvls', [
            'fmind/lvls/0.lv',
            'fmind/lvls/1.lv',
            'fmind/lvls/2.lv',
            'fmind/lvls/3.lv'
        ])
    ],

    entry_points={  # Optional
        "console_scripts": [
            #'sample=sample:main',
            "fastmind=fmind:main"
        ]
    },

    # scripts=["fastmind.py"],

    project_urls={  # Optional
        "Source": "https://github.com/boot1110001/fastmind"
    }
)
