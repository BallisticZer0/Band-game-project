import os				  # Need
from cx_Freeze import setup, Executable   # Need


# The following 4 paths may need to be python3 not python36, in the event that the code doesn't work.

os.environ['TCL_LIBRARY'] = 'c:/python36/tcl/tcl8.6'	# Check that these paths work on each computer this gets installed on
os.environ['TK_LIBRARY'] = 'c:/python36/tcl/tk8.6'	# Also check this path basically need to know these libraries exhist

buildOptions = dict(                                                                  # Need - well in theory
    packages = [],                                                                    # Need 
    excludes = [],                                                                    # Need
    include_files=['c:/python36/DLLs/tcl86t.dll', 'c:/python36/DLLs/tk86t.dll']       # Check these paths and make sure the libraries (The .dll) are there  
)


# In theory this should just tell us that if we are using a 32 bit system make sure to note it other wise we know we should be on 64 bit
import sys
base = 'Win32GUI' if sys.platform=='win32' else None

# Create the actually executable from a given file name that we want the executable to run
executables = [
    Executable('Band game.py', base=base)            # NOTE: If you get an ERROR saying unknown "Band game.py" try "Band/ game.py"
]

setup(name='BandGame',                               # Name of executable
      version = '1.0',                               # The rest is just standard options for how to do the building of exe
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
