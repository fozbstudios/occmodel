Introduction
============

occmodel is a small library which gives a high level access
to the OpenCASCADE modelling kernel.

For most users a direct use of the OpenCASCADE modelling
kernel can be quite a hurdle as it is a huge library.

This is a fork from https://github.com/tenko/occmodel

It has been repackaged so that it installs easily on Ubuntu 14.04 LTS, no other platforms have been or will be tested.


Install
========

 * Python 2.7/3.x and Cython 0.17 or later.
 * A working installation of OpenCASCADE (OCE prefered)

On Ubuntu 14.04, install OpenCASCADE with: 
    sudo apt-get install liboce-*

Then install occmodel with:
    sudo python setup.py install


Documentation
=============

See online Sphinx docs_

.. _docs: http://tenko.github.com/occmodel/index.html

.. _pypi: http://pypi.python.org/pypi/occmodel

.. _OCE: https://github.com/tpaviot/oce/downloads
