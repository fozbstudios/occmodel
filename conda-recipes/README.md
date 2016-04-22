## Introduction

This directory contains the conda recipies for building [occmodel](https://github.com/colonelzentor/occmodel), [VTK 7.0](http://www.vtk.org) and [OpenCASCADE Community Edition (OCE) v0.17.1](https://github.com/tpaviot/oce) against Python 3.5 and Qt4 for Linux.  These recipes assume you have the following packages installed at the system level as there are not conda equivalents for them:

    fedora|redhat|centos:  gcc-c++ mesa-libGLU-devel libXmu-devel tbb-devel
    ubuntu|debian: g++ libglu1-mesa-dev libxmu-dev libtbb-dev

## Building Conda Recipes

To build a given recipe, simply type:

    conda build <recipe directory>

If you then want to install from the local build:

    conda install --use-local <recipe package>

See [Conda Docs >> Building packages](http://conda.pydata.org/docs/building/build.html) for information on how to make, build and install a recipe, or just look at the plethora of examples on the [conda-recipes](https://github.com/conda/conda-recipes) github page.