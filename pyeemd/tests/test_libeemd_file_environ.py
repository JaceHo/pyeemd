# Copyright 2016 Perttu Luukko

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

"""Unit tests for setting the libeemd library file location from an environment
variable"""

import os
from nose.tools import raises
from pyeemd.pyeemd import _init as init

def test_valid_reinit():
    init()

@raises(OSError)
def test_bogus_LIBEEMD_FILE():
    os.environ["LIBEEMD_FILE"] = "completely_bogus_path.so"
    init()
