from __future__ import print_function

# Copyright 2013 Perttu Luukko

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

from pyeemd import bemd
from nose.tools import assert_equal, raises
from numpy import zeros, all, abs, allclose, linspace, sum
from numpy.testing import assert_allclose
from numpy.random import normal, randint
from ctypes import ArgumentError

@raises(TypeError)
def test_bogus1():
    x = bemd("I am a banana")

@raises(ValueError)
def test_bogus2():
    x = bemd(7)

@raises(ValueError)
def test_wrong_dims():
    x = zeros((2,2))
    bemd(x)

@raises(ValueError)
def test_invalid_arguments4():
    x = []
    bemd(x, num_siftings=-3)

@raises(ArgumentError, TypeError)
def test_invalid_arguments6():
    x = []
    bemd(x, num_imfs="Just a few")

@raises(ValueError)
def test_invalid_arguments7():
    x = []
    bemd(x, num_imfs=0)

@raises(ValueError)
def test_invalid_arguments8():
    x = []
    bemd(x, num_imfs=-5)

def test_zeros():
    x = zeros(64, dtype=complex)
    imfs = bemd(x)
    assert all(imfs == 0)

def test_completeness():
    for i in range(8):
        yield check_completeness

def check_completeness():
    N = 64
    x = normal(0, 1, N) + normal(0, 1, N)*1j
    imfs = bemd(x)
    imfsum = sum(imfs, axis=0)
    assert_allclose(x, imfsum)

def test_num_imfs():
    N = 64
    x = normal(0, 1, N) + normal(0, 1, N)*1j
    imfs1 = bemd(x, num_imfs=3)
    imfs2 = bemd(x, num_imfs=4)
    assert_allclose(imfs1[:2,:], imfs2[:2,:])

def test_num_imfs_output_size():
    N = 64
    x = normal(0, 1, N) + normal(0, 1, N)*1j
    imfs = bemd(x, num_imfs=3)
    assert imfs.shape[0] == 3

def test_num_imfs_just_residual():
    N = 64
    x = normal(0, 1, N) + normal(0, 1, N)*1j
    imfs = bemd(x, num_imfs=1)
    assert_allclose(imfs[-1,:], x)
