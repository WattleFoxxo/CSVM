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
: MakeFile
; this is the main folder for the CLI side of CubeScript, this is where the 

python: main.py 
: CubeScriptLexer.py
: CubeScriptParser.py
: CubeScriptListener.py
: CubeScriptVisitor.py
: transpiler3.0.py
: updater.py
: version.py
; this is the main folder of CubeScript, this is where the code is transpiled into CSharp code or any of the supported languages