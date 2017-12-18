
# Copyright 2013 Perttu Luukko

# This file is part of pyeemd.
# 
# pyeemd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# pyeemd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with pyeemd.  If not, see <http://www.gnu.org/licenses/>.

from pyeemd import emd, eemd, emd_find_extrema
from nose.tools import assert_equal, raises
import numpy as np
from numpy import zeros, all, arange, sum, all
from numpy.testing import assert_allclose
from numpy.random import normal

@raises(TypeError)
def test_bogus_arguments1():
    x = normal(0, 1, 128)
    emd(x, noise_strength=1)

@raises(TypeError)
def test_bogus_arguments2():
    x = normal(0, 1, 128)
    emd(x, ensemble_size=100)

def test_emd_is_eemd():
    for i in range(16):
        x = normal(0, 1, 128)
        yield check_emd_is_eemd, x
    
def check_emd_is_eemd(x):
    emd_imfs = emd(x)
    eemd_imfs = eemd(x, ensemble_size=1, noise_strength=0)
    assert all(emd_imfs == eemd_imfs)

def test_empty():
    x = []
    imfs = emd(x)
    assert_equal(imfs.ndim, 2)
    assert_equal(imfs.size, 0)

def test_shorts():
    for n in range(1,4):
        yield check_short, n

def check_short(n):
    x = arange(n)
    imfs = emd(x)
    assert_equal(imfs.ndim, 2)
    assert_equal(imfs.shape[0], 1)
    assert all(imfs[0,:] == x)

def test_identical_data():
    for i in range(8):
        yield check_identical_data

def check_identical_data():
    x = normal(0, 1, 64)
    imfs1 = emd(x, num_siftings=10)
    imfs2 = emd(x, num_siftings=10)
    assert_allclose(imfs1, imfs2)

def test_completeness():
    for i in range(8):
        yield check_completeness

def check_completeness():
    x = normal(0, 1, 64)
    imfs = emd(x)
    imfsum = sum(imfs, axis=0)
    assert_allclose(x, imfsum)

def test_num_imfs():
    N = 64
    x = normal(0, 1, N)
    imfs1 = emd(x, num_imfs=3, num_siftings=10)
    imfs2 = emd(x, num_imfs=4, num_siftings=10)
    assert_allclose(imfs1[:2,:], imfs2[:2,:])

def test_num_imfs_output_size():
    N = 64
    x = normal(0, 1, N)
    imfs = emd(x, num_imfs=3)
    assert imfs.shape[0] == 3

def test_num_imfs_just_residual():
    N = 64
    x = normal(0, 1, N)
    imfs = emd(x, num_imfs=1)
    assert all(imfs[-1,:] == x)

def count_zero_crossings(x):
    signs = np.sign(x)
    signs = signs[signs != 0]
    return np.count_nonzero(np.diff(signs))


def check_imfs_singlemode(x):
    imfs = emd(x, num_siftings=0, S_number=4)
    num_imfs = imfs.shape[0]
    for i in reversed(range(num_imfs-1)): # residual is not tested
        imf = imfs[i,:]
        maxx, maxy, minx, miny = emd_find_extrema(imf)
        # remove extra extrema at the ends of the data
        maxx = maxx[1:-1]
        maxy = maxy[1:-1]
        minx = minx[1:-1]
        miny = miny[1:-1]
        num_extrema = len(minx) + len(maxx)
        num_zc = count_zero_crossings(imf)
        try:
            assert len(miny) + len(maxy) == num_extrema, "Inconsistent number of extrema"
            assert abs(num_zc-num_extrema) <= 1, "Number of zero crossings is %d while number of interior extrema is %d" % (num_zc, num_extrema)
            assert all(miny <= 0), "Positive minima in IMF %d/%d: %s" % (i+1, num_imfs, miny[miny > 0])
            assert all(maxy >= 0), "Negative maxima in IMF %d/%d: %s" % (i+1, num_imfs, maxy[maxy < 0])
        except AssertionError as ae:
            try:
                from matplotlib import pyplot as plt
                plt.figure()
                plt.title(str(ae) + " %d minima, %d maxima, %d zero-crossings" % (len(miny),
                   len(maxy), num_zc))
                plt.plot(imf, 'k-', alpha=0.3)
                plt.plot(maxx, maxy, 'bs')
                plt.plot(minx, miny, 'rx')
                plt.axhline(0, linestyle='dashed', color='black')
                plt.show()
            except ImportError:
                pass
            raise ae


def test_imfs_singlemode_normal():
    for i in range(32):
        x = normal(0, 1, 128)
        check_imfs_singlemode(x)


def test_imfs_singlemode_uniform_discrete():
    for i in range(32):
        x = np.random.randint(low=-5, high=6, size=128)
        check_imfs_singlemode(x)
