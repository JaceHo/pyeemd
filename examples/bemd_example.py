#!/usr/bin/env python

# Copyright 2017 Perttu Luukko

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

"""Example for the bivariate EMD. Should reproduce results shown in Fig. 3 from the original BEMD article by Rilling et al (2007)."""

import numpy as np
import matplotlib.pyplot as plt

from pyeemd import bemd

def plot_complex_signal(s, axis):
    """Common helper function for plotting complex signals"""
    axis.plot(np.real(s), 'b-')
    axis.plot(np.imag(s), 'k--')

# Load example data
data = np.loadtxt("float_position_record.txt.gz")
x = data[:,0]
y = data[:,1]

plt.figure()
plt.xlabel("Displacement East (km)")
plt.ylabel("Displacement North (km)")
plt.plot(x, y)

# Decompose with BEMD
signal = x + y*1j
imfs = bemd(signal, num_siftings=10, num_imfs=4)

# Plot imfs
f, axes = plt.subplots(5, sharex=True)
axes[-1].set_xlabel("Time (days)")

plot_complex_signal(signal, axes[0])
for i in range(4):
    plot_complex_signal(imfs[i], axes[i+1])

plt.show()
