%module {{ cookiecutter.project_name }}

%feature("autodoc", "1");

%{
    #define SWIG_FILE_WITH_INIT
    #include "{{ cookiecutter.project_name }}.h"
%}

%include "stl.i"
%include "numpy.i"

%init %{
    import_array();
%}

// Apply numpy typemaps before %including headers

%include "{{ cookiecutter.project_name }}.h"
