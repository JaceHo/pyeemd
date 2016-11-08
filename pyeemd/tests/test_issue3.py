# Copyright 2016 Perttu Luukko

# This file is part of libeemd.
# 
# libeemd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# libeemd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with libeemd.  If not, see <http://www.gnu.org/licenses/>.

"""Unit tests for pyeemd issue #3"""

from __future__ import print_function

import numpy as np
from pyeemd import ceemdan

def check_residual_is_not_nan(signal):
    out = ceemdan(signal)
    residual = out[-1,:]
    print(residual)
    assert not np.any(np.isnan(residual))

def test_issue3():
    signal = [532.038, 532.467, 532.897, 532.579, 531.834, 531.089, 530.344, 530.243, 529.637, 529.871, 530.586, 531.302, 531.528, 531.674, 531.562, 531.562]
    check_residual_is_not_nan(signal)

def check_random_signal(size):
    signal = np.cumsum(np.random.normal(size=size))
    check_residual_is_not_nan(signal)

def test_random_signals():
    for size in [15, 16, 17, 32, 62]:
        yield check_random_signal, size
