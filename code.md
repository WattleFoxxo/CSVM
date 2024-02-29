# where and what are these extra code folders?

so, your wondering why there are code folders for different coding languages?

heres what's inside and where everything is:

rust: src/main.rs 
: src/lib.rs 
: Cargo.toml 
: Cargo.lock 
; this is the main folder for the project creation side of CubeScript

cpp: src/main.cpp 
: src/main.hpp 
: src/MakeFile
: src/csvm.cpp
: src/CubeScript.hpp
: src/main.pro
; this is the main folder for the CLI side of CubeScript, this is where the main checks and help documentation is not including the help.py file

python: main.py 
: transpiler
: help.py

; this is the main folder of CubeScript, this is where the code is transpiled into CSharp code or any of the supported languages