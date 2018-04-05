import os.path
from setuptools import Extension, find_packages, setup
from setuptools.command.build_py import build_py
from setuptools.command.install import install
import sys


def get_include_dirs():
    """Gets include directories that may require extra packages installed."""
    import numpy as np
    return [np.get_include()]


def get_compile_args():
    """Return extra compiler arguments for building extensions."""
    if sys.platform.startswith('darwin'):
        return ['-std=c++14', '-stdlib=libc++', '-mmacosx-version-min=10.8']
    elif sys.platform.startswith('win'):
        return ['/EHsc']  # exception handling
    elif sys.platform.startswith('linux'):
        return ['-std=c++14']
    else:
        raise RuntimeError("Unknown platform: " + sys.platform)


extensions = [
    Extension(
        "{{ cookiecutter.project_name }}._{{ cookiecutter.project_name }}",
        sources=[
            os.path.join("{{ cookiecutter.project_name }}", filename)
            for filename in [
                "{{ cookiecutter.project_name }}.i",
                "{{ cookiecutter.project_name }}.cpp",
            ]
        ],
        swig_opts=["-c++"],
        include_dirs=get_include_dirs(),
        extra_compile_args=get_compile_args(),
    )
]

setup(
    name="{{ cookiecutter.project_name }}",
    version="{{ cookiecutter.version }}",
    author="{{ cookiecutter.author }}",
    description="{{ cookiecutter.description }}",
    long_description="{{ cookiecutter.long_description }}",
    ext_modules=extensions,
    packages=find_packages(where="{{ cookiecutter.project_name }}"),
)
