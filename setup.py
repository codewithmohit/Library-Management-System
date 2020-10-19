application_title='Library'
main_python_file='work.py'

import sys
from cx_Freeze import setup,Executable
base=None
if sys.platform=="win32":
    base="Win32GUI"

includes=[]
includes_files=['Theme']
setup(
    name=application_title,
    version="1.0",
    description="library",
    options={"build_exe":{"includes":includes,"include_files":includes_files}},
    executables=[Executable(main_python_file,base=base)])
