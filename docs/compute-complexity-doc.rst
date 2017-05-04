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

BASIC USE
---------

To run cmptcomplexity after installation, first, you  have to import module

   >>> import cmptcomplexity.aprox as cmpt

To get information about complexity of sorting list, you could type


   >>> results = cmpt.count_it(pattern_invoke= 'sorted(list)',init_code='import random; list = [random.randint(1,10000) for i in range (__N__)]')

After executing this, you can:

    >>> result.complexity   # returns information about algorithm complexity
    >>> result.show()       # displays plot of measured times
    >>> result.show('~/file.png')       # saves plot of measured times to png file

For more information read `PYTHON INTERFACE`_


.. _`PYTHON INTERFACE`

PYTHON INTERFACE
================

INPUTS
------

The main function (count_it) is included in cmptcomplexity.aprox.


*cmptcomplexity.aprox.*
**count_it(pattern_invoke, init_code, clean_up_code, timeout, verbose)**

Before using this function, is neccesary to preapare a simple strutures for an algorithm:

pattern_invoke
    A pattern of invoking tested function/method/class, with '__N__' as size-problem parameter.
    pattern_invoke could be string or a path to file, where this string is typed.

    example
        Let's assume object **example_object** and method **example_method(arg1, arg2, arg3, arg4)**, where **arg3** is problem-size parameter.
        Proper structure would be like

        >>> pattern_invoke = 'example_object.example_method(arg1,arg2,__N__,arg4)'

        or, when you a have a file **/home/user/dir0/dir1/pattern.py'** with

        .. code-block:: python

            example_object.example_method(arg1,arg2,__N__,arg4)

        assign pattern_invoke to path to this file

        >>> pattern_invoke = '/home/user/dir0/dir1/pattern.py'


init_code(optional)
    This strucure contains a code, which time execution shouldn't be measured.
    The creation of this stucture is similiar to **pattern_invoke**.If you want to test self-defined class/method/function,  in this structure you should include, all definitions of functions

    example
        Let's assume we want deduce a computional complexity of sorting a list. It is necesary to crate a list with random numbers. If it depends on problem size, you have to write '__N__' as an problem-size argument
    >>> init_code = 'import random; list = [random.randint(0,10000) for i in range(__N__)]'

    or, you could also create a *.py file with

    .. code-block:: python

        import random
        list = [random.randint(0,10000) for i in range(__N__)]

    and give a path to file

    >>> init_code = '/home/user/path/to/file.py'

clean_up_code(optional)
    This code would be executed after measuring times. Type a string or path to file.
    example
        .. code-block:: python

        clean_up_code ='import shutil; shutil.rmtree("./temporary_files_tree/")'


timeout
    Sets a time for algorithm in seconds. Default 30s.

log_verbose
    specify a loggeer options

      .. code-block:: python

        log_verbose = True # Puts all logging message to Standard outpt.
        log_verbose = False # Puts only warning message to Standard outpt.
        log_verbose = 'path/to/file.log' #creates a log file at given path

    defalut: True



This structure can be written in file

cmptcomplexity.aprox.count_it(pattern_invoke, init_code="", clean_up_code="", timeout=30, log_verbose=True)::


    pattern_invoke - speciefies a invoking pattern for tested function or class.
    init_code - file path or string with initialization of proper stuctures
RETURN VALUE
------------
count_it(pattern_invoke, init_code, clean_up_code, timeout, verbose) returns an object of Result class, with fields:

.. code-block:: python

    class Result:
        self.complexity `information about complexity of algorithm <- ['O(N), O(N^2)']`
        self.in_time() #returns a function time-> size(time), which count, how big problem can be solved in time msec
        self.how_long() #returns a function n-> time(n), which count, how long it take to solve n - sized problem
        self.show() #shows a plot of mesured, with no argument just show, with file patg as argument saves a *png image


EXAMPLE USES
============

Binary Search
-------------

0) Create a file *init-b-search.py* with content

    .. code-block:: python

        def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False
        while first<=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1
        return found

        import random
        list = [random.randint(0,100000) for i in range(__N__)]

1) Create a file *exec-b-search.py* with content

    .. code-block:: python

        binarySearch(list,random.randint(0,100000))

2) In Python interactive mode type:

    >>> import cmptcomplexity.aprox as ap
    >>> results = ap.countit(pattern_invoke = 'path/to/exec-b-search.py',init_code='path/to/init-b-search.py',timeout=30,log_verbose=True)
    >>> results.show() # shows a graph
    >>> results.max_in_time(100) # counts maximum problem in 100 msec
    >>> results.time_of(23441) # counts time of execution for 23441 problem size

    .. image:: bsresult
        :target: