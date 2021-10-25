import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {"build_exe": {"includes": "atexit"}}

executables = [Executable("Toolloginmail.py", base=base)]

setup(
    name="Toolloginmail",
    version="0.1",
    description="Toolloginmail",
    options=options,
    executables=executables,
)