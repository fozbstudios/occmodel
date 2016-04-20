Introduction
============

This repo is a fork of `mikedh/occmodel <https://github.com/mikehd/occmodel>`_ which itself is a fork of `tenko/occmodel <https://github.com/tenko/occmodel>`_.  This project's primary purpose is for upgrading occmodel to the most recent version of `OpenCASCADE Community Edition <https://github.com/tpaviot/oce>`__ (OCE).  In addition it is going be used to explore using cython to wrap the VTK interface package in the 0.17.1 release of OCE.  `VTK <http://www.vtk.org>`_ provides a superior rendering engine option for OCE topological shapes.

Install into a Conda Environment
================================
The easiest way to install occmodel and it's dependancies into a conda environment is via the conda packages located on `my <https://anaconda.org/colonel_zentor/>`_ Anaconda.org channel .  There you will find packages for occmodel, VTK 7.0 and OCE 0.17.1 all built against Python 3.5 and Qt4.  If you are absolutely bent on building occmodel, VTK and OCE from source check out the conda package recipes in this repo for more information.

Note, VTK and OCE both need the following packages installed at the system level in order to work correctly.  Installation via dnf|yum|apt-get is necessary because there are currently not conda equivalent packages.

    fedora|redhat|centos: mesa-libGLU libXmu tbb
    ubuntu|debian: libglu1-mesa libxmu libtbb

Examples
========
The examples directory contains several `Jupyter <http://jupyter.org/>`_ notebooks showing the ``occmodel`` API in action. The ``OCCT_Bottle_Example.ipynb`` notebook recreates the OpenCASCADE `bottle tutorial <http://dev.opencascade.org/doc/overview/html/occt__tutorial.html>`_ using ``occmodel`` and displays the result in a VTK rendering window. The ``Step_File_import.ipynb`` notebook demonstrates importing and displaying a STEP file.

The examples directory includes a simple Qt-based VTK viewer that can be launched from a Jupyter Notebook.  Eventually this will be replaced with a VTK widget but for the time being this will have to suffice.  

Documentation
=============

See the `tenko/occmodel <https://github.com/tenko/occmodel>`_ Sphinx docs_ for API documentation.  

Currently, the only deviation of this fork from ``tenko/occmodel`` is the addition of ``toVtkActor`` on ``OCCBase`` and the addition of the ``OCCVtk`` package.  The ``OCCVtk`` package only defines one function, ``shapeToActor(Base occShape)``.

.. _docs: http://tenko.github.com/occmodel/index.html
