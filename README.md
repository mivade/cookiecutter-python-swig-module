# cookiecutter-python-swig-module

A [cookiecutter][] for creating [SWIG][]-based Python extensions with built-in
support for Numpy.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[SWIG]: http://www.swig.org/

## What's included

* `setup.py` to build an extension module with C++14 enabled by default and
  using Numpy
* Skeleton header and C++ source files
* Basic SWIG interface file

## Prerequisites

* Swig must be installed for the extension module to build

## Usage

```
$ cookiecutter gh:mivade/cookiecutter-python-swig-module
```
