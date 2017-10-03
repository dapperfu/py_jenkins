# -*- coding: utf-8 -*-
"""Python Setup File."""

# https://setuptools.readthedocs.io/en/latest/setuptools.html#new-and-changed-setup-keywords


import os

from setuptools import setup

requires = {}
for requirement in ["setup", "install", "tests"]:
    requires_txt = os.path.join(
        ".requirements",
        "{}.txt".format(requirement),
    )
    if os.path.exists(requires_txt):
        with open(requires_txt, "r") as f:
            require_pkgs = f.read().splitlines()
        requires[requirement] = require_pkgs

setup(
    name='py_jenkins',
    python_requires='>=2.7,!=3.0.*,!=3.1.*',
    setup_requires=requires["setup"],
    install_requires=requires["install"],
    tests_require=requires["tests"],
    test_suite="pytest",
)
