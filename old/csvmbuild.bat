REM " this is a batch file to build the CSVM.py program"
py -3.11-64  -m  nuitka --onefile  CSVM.py  --windows-icon-from-ico=csvm.ico

REM ' delete the build folders'
rmdir /s /q CSVM.build CSVM.dist CSVM.onefile-build build