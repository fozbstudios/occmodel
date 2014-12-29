#
# File:  Makefile (for library)
#
# The variables 'PYTHON' and 'PYVER' can be modified by
# passing parameters to make: make PYTHON=python PYVER=2.6
#
PYTHON=python2
PYVER=2.7

CC=g++
CFLAGS=-Wall -fPIC -O2 -frtti -fexceptions -Isrc -I/usr/include/oce
LIB=liboccmodel.a
LIBSRC = $(wildcard src/*.cpp)

LIBOBJ=$(LIBSRC:.cpp=.o)

.PHONY: pylib docs test tests install clean

$(LIB): $(LIBOBJ)
	@echo lib Makefile - archiving $(LIB)
	@echo $(AR) r $(LIB) $(LIBOBJ)
	@$(AR) r $(LIB) $(LIBOBJ)

.cpp.o:
	@echo lib Makefile - compiling $<
	@$(CC) $(CFLAGS) -c $< -o $@

pylib: $(LIB)
	@echo lib Makefile - building python extension
	$(PYTHON) setup_build.py build_ext --inplace --force

clean:
	-rm $(LIBOBJ)
	-rm $(LIB)
	-rm -rf build dist
	-rm -rf occmodel/@docs/build
	-rm MANIFEST occmodel/@src/Config.pxi
	-rm occmodel.dll occmodel.so occmodel/occmodel.cpp
	-rm occmodelviewer.dll occmodelviewer.so occmodel/occmodelviewer.c
	-find occmodel -iname '*.so' -exec rm {} \;
	-find occmodel -iname '*.pyc' -exec rm {} \;
	-find occmodel -iname '*.pyo' -exec rm {} \;
	-find occmodel -iname '*.pyd' -exec rm {} \;
