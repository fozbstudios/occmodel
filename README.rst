Introduction
============

This repo is a fork of `mikedh/occmodel <https://github.com/mikehd/occmodel>`_ which itself is a fork of `tenko/occmodel <https://github.com/tenko/occmodel>`_.  This project's primary purpose is for upgrading occmodel to the most recent version of `OpenCASCADE Community Edition <https://github.com/tpaviot/oce>`__ (OCE).  In addition it is going be used to explore using cython to wrap the VTK interface package in the 0.17 release of OCE.  `VTK <http://www.vtk.org>`_ provides a superior rendering engine option for OCE topological shapes.

Install
========
Since this code is to be built against the most recent version of OCE, you will most likely need to build OCE from source. See below for detailed instructions.  There is also a dependency on VTK, you can either install VTK via yum/apt-get or build it yourself.  I would recommend building it yourself as installing VTK via a package manager pulls along a ton of other packages (at least in Fedora it does) that you most likely don't need at this time.  If and when the conda VTK package is updated to 6.x from 5.10, you will also be able to build OCE against that, in the mean time see below for VTK build instructions.

Note, rather than installing OCE and VTK into the the default location (``/usr/local``), I'm using an alternative location (``/opt/cad-lib``) to make it easier to update and/or uninstall if need be.

Building VTK:
-------------

VTK Required Packages:  ``cmake gcc-c++ mesa-libGLU-devel libXmu-devel python-devel``

* If building VTK with Qt4 integration add:  ``qt-devel qt-webkit-devel``
* If building VTK with Qt5 integration add:  ``qt5-qtbase-devel qt5-qttools-devel qt5-qtwebkit-devel``

Optional Packages:  ``cmake-gui doxygen graphviz-devel``

#. ``git clone https://github.com/Kitware/VTK.git``
#. ``cd VTK; git checkout -b v6.2.0 tags/v6.2.0``
#. ``mkdir build-v6.2.0; cd build-v6.2.0``
#. CMake command for building with Qt4:
    | ``cmake \``
    | ``-DVTK_QT_VERSION:STRING=4 \``
    | ``-DCMAKE_INSTALL_PREFIX:PATH=/opt/cad-lib/vtk-6.2 \``
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
    | ``-DCMAKE_INSTALL_PREFIX:PATH=/opt/cad-lib/vtk-6.2 \``
    | ``-DQT_QMAKE_EXECUTABLE:PATH=/usr/bin/qmake-qt5 \``
    | ``-DVTK_Group_Qt:BOOL=ON \``
    | ``-DCMAKE_PREFIX_PATH:PATH=/usr/lib64/cmake/Qt5WebKitWidgets/Qt5WebKitWidgetsConfig.cmake  \``
    | ``-DBUILD_SHARED_LIBS:BOOL=ON \``
    | ``-DCMAKE_BUILD_TYPE:STRING=RELEASE \``
    | ``-DVTK_WRAP_PYTHON:BOOL=ON \``
    | ``-DBUILD_DOCUMENTATION:BOOL=OFF \``
    | ``..``
#. ``make -j$(nproc)``
#. ``make install``

To install the python bindings into a virtualenv, activate your desired virtuaenv and run:
    ``add2virtualenv /opt/cad-lib/vtk-6.2/lib/python2.7/site-packages``

If you want to use this build of VTK as you default VTK package you may also want to do the following things:
    #. Create a conf file in ``/etc/ld.so.conf.d``
        ``su -c "echo '/opt/cad-lib/vtk-6.2/lib' >> /etc/ld.so.conf.d/vtk.conf"``
    #. Simlink the VTK header file directory to ``/usr/include``
        ``ln -s /opt/cad-lib/vtk-6.2/include/vtk-6.2 /usr/include``
    #. And in some situations you may need to add VTK libray directory to the ``LD_LIBRARY_PATH`` variable in your ``.bash_profile``.
        ``LD_LIBRARY_PATH=/opt/cad-lib/oce-0.17/lib:$LD_LIBRARY_PATH``

Building OCE:
-------------

OCE Required Packages:  ``cmake gcc-c++ mesa-libGLU-devel freetype-devel tbb-devel``

* If you don't want to build VTK yourself add ``vtk-qt-python`` to the OCE reqired packages list and remove the ``DVTK_DIR:PATH`` setting in the OCE CMake command.

#. ``git clone https://github.com/tpaviot/oce.git``
#. ``cd oce; git checkout -b OCE-0.17 tags/OCE-0.17``
#. ``mkdir build-OCE-0.17; cd build-OCE-0.17``
#. | ``cmake \``
   | ``-DOCE_WITH_VTK:BOOL=ON \``
   | ``-DVTK_DIR:PATH=/opt/cad-lib/vtk-6.2/lib/cmake/vtk-6.2 \``
   | ``-DOCE_MULTITHREAD_LIBRARY:STRING=TBB \``
   | ``-DOCE_INSTALL_PREFIX:PATH=/opt/cad-lib/oce-0.17 \``
   | ``..``
#. ``make -j$(nproc)``
#. ``make install``

If you want to use this build of OCE as you default OCE package you may also want to do the following things:
    #. Create a conf file in ``/etc/ld.so.conf.d``
        ``su -c "echo '/opt/cad-lib/oce-0.17/lib' >> /etc/ld.so.conf.d/oce-0.17.conf"``
    #. Simlink the oce header file directory to ``/usr/include``
        ``ln -s opt/cad-lib/oce-0.17/include /usr/include``
    #. And in some situations you may need to add the OCE libray directory to the ``LD_LIBRARY_PATH`` variable in your ``.bash_profile``.
        ``LD_LIBRARY_PATH=/opt/cad-lib/oce-0.17/lib:$LD_LIBRARY_PATH``

Then install occmodel with:

    ``pip install git+https://github.com/colonelzentor/occmodel.git``

Or if you want the source on your computer:

    ``git clone https://github.com/mikedh/occmodel.git``

    ``cd occmodel``

    ``python setup.py install``


Documentation
=============

See online Sphinx docs_ for docs for `tenko/occmodel <https://github.com/tenko/occmodel>`_.

.. _docs: http://tenko.github.com/occmodel/index.html
