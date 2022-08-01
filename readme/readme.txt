Formatter for CudaText.
It allows to format (beautify) source code for lexers C, C++, C#, Java, using AStyle library.

Plugin has configuration file. It's single-line text file with AStyle command-line options, see them at: 
http://astyle.sourceforge.net/astyle.html


Installation on Linux and Unix'es
---------------------------------
Plugin requires "pyastyle" Python library. Install it like this:
$ pip3 install pyastyle


Installation on Windows
-----------------------
Download the package from https://pypi.org/project/pyastyle/#files
according to CudaText bitness (32- or 64-bit) and Python version.
Seems that site doesn't have the version for Python 3.8, so find
the package elsewhere.
The .whl files are ZIP files, so just unzip them.
Unzip folder "pyastyle" to the folder [CudaText]/py, so you
must have the file "[CudaText]/py/pyastyle/__init__.py".


Author: Alexey Torgashin (CudaText)
License: MIT
