# -*- coding: utf-8 -*-
"""Tests 1."""

import random
import time


def test_hello():
    """Hello."""
    print("World!")


def test_slow():
    """Artificial delayed test."""
    time.sleep(random.randint(0, 10))
