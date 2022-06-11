#
# File:  Makefile (for library)
#
# The variable CONDA_ENV_PATH can be modified by
# passing parameters to make: make CONDA_ENV_PATH=<path to conda env>
#

CONDA_ENV_PATH=$$(conda info | grep 'default environment' | awk '{print $$4}')
OCE_INCLUDE_DIR=${CONDA_ENV_PATH}/include/oce
PYTHON_INCLUDE_DIR=${CONDA_ENV_PATH}/include/python3.8.8
VTK_INCLUDE_DIR=${CONDA_ENV_PATH}/include/vtk-9.1.0

CC=g++
CFLAGS=-Wall -fPIC -O2 -frtti -fexceptions -Isrc -I${OCE_INCLUDE_DIR} -I${PYTHON_INCLUDE_DIR} -I${VTK_INCLUDE_DIR}
LIB=liboccmodel.a
LIBSRC = $(wildcard src/*.cpp)

LIBOBJ=$(LIBSRC:.cpp=.o)

.PHONY: install clean

print-%  : ; @echo $* = $($*)

$(LIB): $(LIBOBJ)
	@echo lib Makefile - archiving $(LIB)
	@echo $(AR) r $(LIB) $(LIBOBJ)
	@$(AR) r $(LIB) $(LIBOBJ)

.cpp.o:
	@echo lib Makefile - compiling $<
	@$(CC) $(CFLAGS) -c $< -o $@

clean:
	-rm $(LIBOBJ)
	-rm $(LIB)
	-rm -rf ../build ../dist
	-rm occmodel.cpp
	-find geotools -iname 'geotools.c' -exec rm {} \;
	-find occmodel -iname '*.so' -exec rm {} \;
	-find occmodel -iname '*.pyc' -exec rm {} \;
	-find occmodel -iname '*.pyo' -exec rm {} \;
	-find occmodel -iname '*.pyd' -exec rm {} \;
