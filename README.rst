Introduction
============

occmodel is a small library which gives a high level access
to the OpenCASCADE modelling kernel. For most users direct use of the OpenCASCADE modelling kernel is undesirable as it is large and opaque. 

This is a fork from https://github.com/tenko/occmodel

It has been repackaged and pared down so that it installs easily on Ubuntu 14.04 LTS, no other platforms have been or will be tested. 


Install
========

On Ubuntu 14.04, install OpenCASCADE with: 

    sudo apt-get install liboce-*

Then install occmodel with:

    sudo pip install git+https://github.com/mikedh/occmodel.git

Or if you want the source on your computer:

    git clone https://github.com/mikedh/occmodel.git

    cd occmodel

    sudo python setup.py install


Documentation
=============

See online Sphinx docs_

.. _docs: http://tenko.github.com/occmodel/index.html

.. _pypi: http://pypi.python.org/pypi/occmodel

.. _OCE: https://github.com/tpaviot/oce/downloads
