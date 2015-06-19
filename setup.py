#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "THE WISKEY-WARE LICENSE":
# Juan BC <jbc.develop@gmail.com>
# wrote this file. As long as you retain this notice you can do whatever you
# want with this stuff. If we meet some day, and you think this stuff is worth
# it, you can buy me a WISKEY in return Juan BC


#==============================================================================
# DOCS
#==============================================================================

"""This file is for distribute django-repo-gallery with distutils

"""

# =============================================================================
# CONSTANTS
# =============================================================================

REQUIRES = ["django>=1.8"]


# =============================================================================
# FUNCTIONS
# =============================================================================

if __name__ == "__main__":
    import os
    import sys

    from ez_setup import use_setuptools
    use_setuptools()

    from setuptools import setup, find_packages

    setup(
        name="django-repogallery",
        version="0.0.1",
        description="Create galleries from code repository",
        author="JuanBC",
        author_email="jbc.develop@gmail.com",
        url="http://repogallery.jbcabral.org/",
        license="WISKEY-WARE",
        keywords="scm gallery git hg mercurial svn".split(),
        classifiers=[],
        packages=[
            pkg for pkg in find_packages() if pkg.startswith("repogallery")],
        include_package_data=True,
        py_modules=["ez_setup"],
        install_requires=REQUIRES,
    )
