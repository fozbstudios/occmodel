#!/bin/bash

# assumes you have 
#    fedora/redhat/centos:  gcc-c++ mesa-libGLU-devel libXmu-devel tbb-devel 
#    ubuntu/debian: g++ libglu1-mesa-dev libxmu-dev libtbb-dev
# installed a the system level as there are not conda equivalents for these packages.

mkdir build; cd build

cmake \
-DCMAKE_INSTALL_PREFIX:PATH=${PREFIX} \
-DVTK_WRAP_PYTHON:BOOL=ON \
-DVTK_PYTHON_VERSION:STRING=3 \
-DVTK_Group_Web:BOOL=OFF \
-DVTK_Group_Qt:BOOL=ON \
-DVTK_QT_VERSION:STRING=4 \
-DQT_QMAKE_EXECUTABLE:PATH=${PREFIX}/bin/qmake \
-DCMAKE_PREFIX_PATH:PATH=/usr/lib64/cmake \
-DBUILD_SHARED_LIBS:BOOL=ON \
-DCMAKE_BUILD_TYPE:STRING=RELEASE \
-DBUILD_TESTING:BOOL=OFF \
-DBUILD_DOCUMENTATION:BOOL=OFF \
-DVTK_SMP_IMPLEMENTATION_TYPE:STRING=TBB \
-DVTK_RENDERING_BACKEND:STRING=OpenGL2 \
..

make -j $(nproc)
make install