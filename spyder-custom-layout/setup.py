# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Bot
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Custom Layout setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_custom_layout import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-custom-layout",
    version=__version__,
    author="Spyder Bot",
    author_email="spyder.python@gmail.com",
    description="Example plugin that register a programmatic custom layout",
    license="MIT license",
    url="https://github.com/spyder-bot/spyder-custom-layout",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.0.4",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_custom_layout = spyder_custom_layout.spyder.plugin:SpyderCustomLayout"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
