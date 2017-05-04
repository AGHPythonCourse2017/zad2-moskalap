CMPTCOMPLEXITY
++++++++++++++



.. Contents::


INTRODUCTION
============


cmptcomplexity is a Python module, providing a way to deduce computational complexity of given bits of Python code.



PREREQUISITES
=============

cmptcomplexity requires the following software installed for your platform:


0) UNIX-like system supporting signal communication

1) Python__ 2.7 or >= 3.4

__ http://www.python.org

2) NumPy__ >= 1.8.2

__ http://www.numpy.org/

3) MatPlotLib__

__ http://matplotlib.org/

4) --optional-- Scipy__

__ http://matplotlib.org/

INSTALLING CMPTCOMPLEXITY
=========================

Development version from Git
----------------------------
Use the command::

  pip3 install git+https://github.com/AGHPythonCourse2017/zad2-moskalap.git

UNINSTALLING
============
Type::

  pip3 uninstall cmptcomplexity


USING CMPTCOMPLEXITY
====================
cmptcomplexity

To run cmptcomplexity after installation, first, you  have to import module

   >>> import cmptcomplexity.aprox as cmpt

   >>> result = cmpt.count_it()



   >>> result.show()

PYTHON INTERFACE
================

The main function (count_it) is included in cmptcomplexity.aprox
Before using this function, is neccesary to preapare a simple strutures for an algorithm:

pattern_invoke
    A pattern of invoking tested function/method/class, with '__N__' as size-problem parameter.

init_code(optional)
    clean_up_code(optional):

This structure can be written in file

cmptcomplexity.aprox.count_it(pattern_invoke, init_code="", clean_up_code="", timeout=30, log_verbose=True)::


    pattern_invoke - speciefies a invoking pattern for tested function or class.
    init_code - file path or string with initialization of proper stuctures

