#!/usr/bin/env python
# Script to generate PC speaker gun sound.

from __future__ import print_function, division, unicode_literals
import random

LEN = 30
MIN = 10
MAX = 25

# Random noise generator that converges toward the lowest frequency.
for i in range(LEN):
	ceil = MAX - (i * (MAX - MIN) / LEN)
	print(random.randint(MIN, int(ceil)))

