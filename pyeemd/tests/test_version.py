# Copyright 2017 Perttu Luukko

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

"""Unit test for pyeemd issue #5"""

from distutils.version import StrictVersion
import pyeemd


def test_pyeemd_version():
    StrictVersion(pyeemd.__version__)
