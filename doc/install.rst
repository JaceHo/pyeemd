.. _installing:

Installing pyeemd
=================

The `pyeemd` module comes with a regular Python `setuptools` installation script,
so installing it should be quite straightforward. The only catch is that you
first need install `libeemd`, since `pyeemd` is only a wrapper for that
library. Please see the ``README`` file distributed with `libeemd` for more
details.

The `pyeemd` module expects to find the file ``libeemd.so`` either in the same
directory as ``pyeemd.py``, or somewhere where `ctypes.util.find_library` will
find it (most notably directories listed in the ``LIBRARY_PATH`` environment
variable). You can also force `pyeemd` to use a specific file by setting the
``LIBEEMD_FILE`` environment variable.

To install `pyeemd` please run::

    python setup.py install

In the top-level directory of `pyeemd` (the one with ``setup.py``).

If you want to specify an alternative installation prefix, you can do it as follows::

    python setup.py install --prefix=$HOME/usr

To make sure everything is working correctly, it is a good idea to run the
supplied unit tests with::

    python setup.py test
