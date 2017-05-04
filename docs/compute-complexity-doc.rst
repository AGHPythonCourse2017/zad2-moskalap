CMPTCOMPLEXITY
++++++++++++++



.. Contents::


INTRODUCTION
============


cmptcomplexity is a Python module for


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


To run cmptcomplexity after installation, execute in Python

   >>> import cmptcomplexity.aprox as cmpt
   >>> result = cmpt.count_it()



   >>> result.show()