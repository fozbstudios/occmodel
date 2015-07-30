Introduction
============

This repo is a fork of `mikedh/occmodel <https://github.com/mikehd/occmodel>`_ which itself is a fork of `tenko/occmodel <https://github.com/tenko/occmodel>`_.  This project's primary purpose is for upgrading occmodel to the most recent version of `OpenCASCADE Community Edition <https://github.com/tpaviot/oce>`__ (OCE).  In addition it is going be used to explore using cython to wrap the VTK interface package in the 0.17 release of OCE.  `VTK <http://www.vtk.org>`_ provides a superior rendering engine option for OCE topological shapes.

Install into a Conda Environment
================================
Note, the following instructions are specifically for building and installing VTK, OCE and occmodel into a Conda environment.

Since this code is to be built against the most recent version of OCE, you will most likely need to build OCE from source. See below for detailed instructions.  There is also a dependency on VTK, you can either install VTK via yum/apt-get or build it yourself.  I would recommend building it yourself as installing VTK via a package manager pulls along a ton of other packages (at least in Fedora it does) that you most likely don't need at this time.  If and when the conda VTK package is updated to 6.x from 5.10, you will also be able to build OCE against that, in the meantime see below for VTK build instructions.

The following instructions are only for building and installing on Linux (specifically Fedora). Windows and Mac users will need to adjust as necessary.  I have not tried to build and install VTK, OCE or occmodel on Windows or Mac and have no idea how to go about doing that.

Building VTK:
-------------

VTK Required Packages:  ``cmake gcc-c++ mesa-libGLU-devel libXmu-devel python-devel``

* If building VTK with Qt4 integration add:  ``qt-devel qt-webkit-devel``
* If building VTK with Qt5 integration add:  ``qt5-qtbase-devel qt5-qttools-devel qt5-qtwebkit-devel``

Optional Packages:  ``cmake-gui doxygen graphviz-devel``

#. ``git clone https://github.com/Kitware/VTK.git``
#. ``cd VTK; git checkout -b v6.2.0 tags/v6.2.0``
#. ``mkdir build-v6.2.0; cd build-v6.2.0``
#. ``ACTIVE_ENV_PATH=$(conda info | grep 'default environment' | awk '{print $4}')``
#. CMake command for building with Qt4:
    | ``cmake \``
    | ``-DVTK_QT_VERSION:STRING=4 \``
    | ``-DCMAKE_INSTALL_PREFIX:PATH=$ACTIVE_ENV_PATH \``
    | ``-DQT_QMAKE_EXECUTABLE:PATH=/usr/bin/qmake-qt4 \``
    | ``-DVTK_Group_Qt:BOOL=ON \``
    | ``-DBUILD_SHARED_LIBS:BOOL=ON \``
    | ``-DCMAKE_BUILD_TYPE:STRING=RELEASE \``
    | ``-DVTK_WRAP_PYTHON:BOOL=ON \``
    | ``-DBUILD_DOCUMENTATION:BOOL=OFF \``
    | ``..``
#. CMake command for building with Qt5:
    | ``cmake \``
    | ``-DVTK_QT_VERSION:STRING=5 \``
    | ``-DCMAKE_INSTALL_PREFIX:PATH=$ACTIVE_ENV_PATH \``
    | ``-DQT_QMAKE_EXECUTABLE:PATH=/usr/bin/qmake-qt5 \``
    | ``-DVTK_Group_Qt:BOOL=ON \``
    | ``-DCMAKE_PREFIX_PATH:PATH=/usr/lib64/cmake \``
    | ``-DBUILD_SHARED_LIBS:BOOL=ON \``
    | ``-DCMAKE_BUILD_TYPE:STRING=RELEASE \``
    | ``-DVTK_WRAP_PYTHON:BOOL=ON \``
    | ``-DBUILD_DOCUMENTATION:BOOL=OFF \``
    | ``..``
#. ``make -j$(nproc)``
#. ``make install``


Building OCE:
-------------

OCE Required Packages:  ``cmake gcc-c++ mesa-libGLU-devel freetype-devel tbb-devel``

If you don't want to build VTK yourself per the instructions above, add ``vtk-qt-python`` to the OCE required packages list and remove the ``DVTK_DIR:PATH`` setting in the OCE CMake command.

#. ``git clone https://github.com/tpaviot/oce.git``
#. ``cd oce; git checkout -b OCE-0.17 tags/OCE-0.17``
#. ``mkdir build-OCE-0.17; cd build-OCE-0.17``
#. ``ACTIVE_ENV_PATH=$(conda info | grep 'default environment' | awk '{print $4}')``
#. OCE CMake Command:
    | ``cmake \``
    | ``-DOCE_WITH_VTK:BOOL=ON \``
    | ``-DVTK_DIR:PATH=$ACTIVE_ENV_PATH/lib/cmake/vtk-6.2 \``
    | ``-DOCE_MULTITHREAD_LIBRARY:STRING=TBB \``
    | ``-DOCE_INSTALL_PREFIX:PATH=$ACTIVE_ENV_PATH \``
    | ``..``
#. ``make -j$(nproc)``
#. ``make install``


Building and installing occmodel:
---------------------------------

To install occmodel into the active virtual environment, simply execute:

    ``pip install git+https://github.com/colonelzentor/occmodel.git``

Or if you want the source on your computer for additional hacking:

    ``git clone https://github.com/colonelzentor/occmodel.git``

    ``cd occmodel``

    ``python setup.py install``

Note, if you are hacking on occmodel and want a clean build each time you install, run:
    
    ``python setup.py build_all;  python setup.py install``

``build_all`` executes ``make clean`` which will remove the build directory and any ``.so``, ``.o``, ``.pyo``, ``.pyc`` and ``.pyd`` files create during a previous build process.


Examples
========
The examples directory contains several Jupyter notebooks showing the ``occmodel`` API in action. The ``OCCT_Bottle_Example.ipynb`` notebook recreates the OpenCASCADE `bottle tutorial <http://dev.opencascade.org/doc/overview/html/occt__tutorial.html>`_ using ``occmodel`` and displays the result in a VTK rendering window. The ``Step_File_import.ipynb`` notebook demonstrates importing and displaying a STEP file.

The examples directory includes a simple Qt4-based VTK viewer.  To use the viewer you will need to install `PySide <https://pypi.python.org/pypi/PySide>`_ into the active conda environment. The following command will build PySide against the system level installed Qt4.

    ``pip install pyside --install-option "--qmake=/usr/bin/qmake-qt4" --install-option "--jobs=$(nproc)" -v``

Documentation
=============

See the `tenko/occmodel <https://github.com/tenko/occmodel>`_ Sphinx docs_ for API documentation.  

Currently, the only deviation of this fork from ``tenko/occmodel`` is the addition of ``toVtkActor`` on ``OCCBase`` and the addition of the ``OCCVtk`` package.  The ``OCCVtk`` package only defines one function, ``shapeToActor(Base occShape)``.

.. _docs: http://tenko.github.com/occmodel/index.html
