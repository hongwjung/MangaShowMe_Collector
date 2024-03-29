from cx_Freeze import setup, Executable
import sys

buildOptions = dict(
	packages = ["PyQt5","sys","bs4","requests","os",\
    "PIL","idna.idnadata","shutil","threading","xml","selenium"], 
	excludes = ["tkinter", "sqlite3"])

base = None
if sys.platform == "win32": #windows GUI 일경우 
    base = "Win32GUI"
    #base = "Console"

exe = [Executable("main.py", base=base,  targetName="MSM.exe")]

setup(
    name='IML MangaShowMe Collector',
    version = '0.1',
    author = "IML",
    description = "I'M IML!",
    options = dict(build_exe = buildOptions),
    executables = exe
)