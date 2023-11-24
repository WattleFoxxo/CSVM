# ProtoGram Compiler

Welcome to the official repo of the CubeScript compiler called CSVM.

## What is CSVM?

CSVM is the name of the Compiler/Transpiler whatever you want to call it, that compiles CubeScript to C#.

Now, i wonder why i chose C#? well, i chose C# because it's a very powerful language and it's very easy to use.
plus the Syntax is roughly within the same range as CubeScript.

## How to use CSVM?

Very simple, just download the latest release from the [releases](https://CubeScript.vercel.app/Download) page and extract the Zip file.

within the zip file contains 4 things, a Readme.txt, CSVM.exe, Home.dll and a Vscode extension that Highlights the Code.

to compile a file, just open up a command prompt and type in `./CSVM <file> <Compiler flags>`

## Compiler Flags

Compiler flags are flags that you can use to change the way the compiler works.

now, you dont need to pass a file when wanting to pass a flag to the compiler, you can just pass the flag and it will work.
unless the flag has a * next to it, which indecates that a file Must be passed.

here is a list of all the flags that you can use:

```txt
using -o <file> will output the compiled code to a file so that you can read the resoulting output. * 
using -t will Open a terminal that will allow you to view help documentation within CSVM.
using -help will show you all the available compiler flags.
using -ve will show you the version of CSVM.
using -v will show you the verbose output of the compiler.
using -c will compile the code and output a EXE or Dll depending what project you created. * 
using -r will compile and run the code. * 
```

## How to use the VSCode extension?

The VSCode extension is a extension that highlights the code for you, so that you can see what you are doing without that stupid 'i'm a text file' type stuff.

to install the extension, just open up the Extensions tab and click on the 3 dots and click on 'Install from VSIX' and select the VSIX file.

altenitively you can follow this youtube video: [How to install a VSIX file](https://www.youtube.com/watch?v=Z724l3mq2ag)

## Why is there a Dll file within the folder?

So, Home.dll contains everything that is needed to Run CubeScript Code, it's like the stdlib of CubeScript.

when using Home.dll, for some reason when importing, you must use 'using static Home;' so that you can use the functions within the dll.

## why not include a libs folder?

Since Home.dll is the only library that is available for CubeScript, i decided to not include a libs folder.

if there ever is more then one library, then i will include a libs folder.

## What is CubeScript?

CubeScript is a programming language designed to make coding easy and better.
you can visit the [CubeScript website](https://cubescript.vercel.app) for more information.


# thanks

thanks to david callahan for the tutorial on how to make a compiler: [Make YOUR OWN Programming Language](https://www.youtube.com/watch?v=Eythq9848Fg)
ive gone and used some of his code located here: [GitHub](https://github.com/davidcallanan/py-myopl-code)

thanks to david for making a easy to understand tutorial!