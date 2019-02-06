#!/usr/bin/python3
#compile
#by boot1110001

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [
    Extension("fastmind", ["fastmind.py"]),
    Extension("core", [
        "core/func.py",
        "core/map.py"
    ]),
    Extension("graphics", [
        "graphics/color.py",
        "graphics/displays.py",
        "graphics/goal.py",
        "graphics/player.py",
        "graphics/rectangle.py",
        "graphics/square.py",
        "graphics/wall.py"
    ])
]

setup(
    name = 'fastmind',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
