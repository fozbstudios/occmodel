#!/bin/bash

# assumes you have 
#    fedora/redhat/centos:  gcc-c++ tbb-devel 
#    ubuntu/debian: g++ libtbb-dev
# installed a the system level as there are not conda equivalents for these packages.

mkdir build; cd build

cmake \
-DOCE_WITH_VTK:BOOL=ON \
-DVTK_DIR:PATH=${PREFIX}/lib/cmake/vtk-7.0 \
-DOCE_MULTITHREAD_LIBRARY:STRING=TBB \
-DOCE_INSTALL_PREFIX:PATH=${PREFIX} \
..

make -j $(nproc)
make install