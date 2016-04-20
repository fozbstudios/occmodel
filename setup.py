#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
# This file is part of occmodel - See LICENSE.txt
#
VERSION = 1,2,0

import sys
import os
import glob
import shutil
import subprocess

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

def version_str():
    return str(VERSION)[1:-1].replace(', ', '.')

def build_libocc():
    subprocess.check_call('cd occmodel; make -j4', shell=True)

class OCCBuild(build_ext):
    def run(self):
        build_libocc()
        build_ext.run(self) 

def build_libocc_clean():
    subprocess.check_call('cd occmodel; make clean; make -j4', shell=True)

class OCCBuildAll(build_ext):
    def run(self):
        build_libocc_clean()
        build_ext.run(self)

# create config file
sys.dont_write_bytecode = True

CONFIG = 'occmodel/src/Config.pxi'
if not os.path.exists(CONFIG) and 'sdist' not in sys.argv:
    with open(CONFIG, 'w') as fh:
        fh.write("__version__ = '%s'\n" % version_str())
        fh.write("__version_info__ = (%d,%d,%d)\n" % VERSION)

OCC_LIB_LIST = \
'''FWOSPlugin PTKernel TKBO TKBRep TKBinL TKBool TKCDF TKFeat TKFillet
TKG2d TKG3d TKGeomAlgo TKGeomBase TKHLR TKIGES TKLCAF TKMath TKMesh TKOffset
TKPLCAF TKPShape TKPrim TKSTEP TKSTEP209 TKSTEPAttr TKSTEPBase TKSTL TKShHealing
TKShapeSchema TKStdLSchema TKTObj TKTopAlgo TKXMesh TKXSBase TKXmlL TKernel TKIVtk
'''

# platform specific settings
SOURCES = ["occmodel/occmodel.pyx"]

OBJECTS, LIBS, LINK_ARGS, COMPILE_ARGS = [],[],[],[]

python_interp_path = sys.executable
conda_env_bin = os.path.split(python_interp_path)[0]
conda_env_base = conda_env_bin.split('/bin')[0]

# If the oce or vtk include paths change, don't forget to update the Makefile...lame
OCC_INCLUDE = os.path.join(conda_env_base, 'include', 'oce')
VTK_INCLUDE = os.path.join(conda_env_base, 'include', 'vtk-7.0')

OCC_LIB_DIR = os.path.join(conda_env_base, 'lib')
OCC_LIBS = list(map(lambda s: OCC_LIB_DIR + "/" + s, OCC_LIB_LIST.split()))

OBJECTS = ["occmodel/liboccmodel.a"]
COMPILE_ARGS.append("-fpermissive")

EXTENSIONS = [
    Extension("geotools",
              sources = ["occmodel/geotools/geotools.pyx",],
              depends = glob.glob("occmodel/geotools/*.pxi") + \
              glob.glob("occmodel/geotools/*.pxd") + \
              glob.glob("occmodel/geotools/*.h"),
              include_dirs = ['occmodel/geotools/',],
          ),
    Extension("occmodel",
              sources = SOURCES,
              depends = glob.glob("occmodel/src/*.pxd") + \
                        glob.glob("occmodel/src/*.pxi"),
              include_dirs = ['occmodel/src', OCC_INCLUDE, VTK_INCLUDE],
              library_dirs = ['/lib/','occmodel'],
              libraries = LIBS + OCC_LIBS,
              extra_link_args = LINK_ARGS,
              extra_compile_args = COMPILE_ARGS,
              extra_objects = OBJECTS,
              language="c++",
          )
]

classifiers = '''\
Development Status :: 4 - Beta
Environment :: Linux
Intended Audience :: Science/Research
License :: OSI Approved :: GNU General Public License v2 (GPLv2)
Operating System :: OS Independent
Programming Language :: Cython
Topic :: Scientific/Engineering
'''

setup(
    name             = 'occmodel',
    version          = version_str(),
    description      = 'Easy access to the OpenCASCADE library',
    long_description =  \
    '''**occmodel** is a small library which gives a high level access
    to the OpenCASCADE modelling kernel.

    For most users a direct use of the OpenCASCADE modelling
    kernel can be quite a hurdle as it is a huge library.

    In order to complete the installation OpenCASCADE must be installed
    on the system. Check the home page or the README file for details.
    ''',
    classifiers  = [value for value in classifiers.split("\n") if value],
    author       = 'Runar Tenfjord',
    author_email = 'runar.tenfjord@gmail.com',
    license      = 'GPLv2',
    url          = 'http://github.com/colonelzentor/occmodel',
    platforms    = ['any'],
    ext_modules  = EXTENSIONS,
    cmdclass     = {'build_ext': OCCBuild, "build_all": OCCBuildAll},
)
