# CubeScript language specification

dated november 23 2023

-----

## Introduction

CubeScript is a Upgrade to CSharp, Sort of how typescript is to javascript.

CubeScript is a language that compiles to CSharp, and is designed to be a more robust language that allows developers that work in multiple programming languages to join in on one codebase.

you can think about how CSharp is to C++ as CubeScript is to CSharp.

CubeScript allows people to write code in a more functional way, and allows programmers from these fields to work on the same codebase.

* python
* javascript
* typescript
* CSharp
* c++
* java
* kotlin
* bython

## Syntax

CubeScript uses a syntax that is similar to CSharp, but with some changes.

Most notibly that the Standard library is not imported by default, and that the syntax is more functional.

CubeScript allows CSharp Code to be ran wthin the codebase, and allows for the use of CSharp libraries, to provide backwards compatibility.

when using CubeScript, the CSVM transpiler might get a bit angry at you, but thats all the fun, right?

just like how TypeScript has that one angry compiler, CubeScript unfortunatly doesnt allow you to change the strictness of the compiler, but it does allow you to use CSharp code, so you can just use that if you want to.

## CSVM

now, you might be wondering, what is CSVM?

just how java has the JVM, CubeScript has the CSVM.

unfortunatly, the CSVM[cubescript virtual machine] doesnt compile to bytecode, but instead compiles to CSharp, which in turn compiles to an executible or a library.

## Standard Library

the standard library is a library that is imported by default, and is used to provide basic functionality to the language.

i've given all the libraries a sort of name that doesnt sound like that total junk microsoft has made for there libraries.

the current list of libraries are:

* Home
* internet

more are to be added in the future.

## How to Make a CubeScript Program

to make a CubeScript program, you need to make a file with the extension `.cusp` , write some code within the file that conforms to the standard we will be setting, and then run ./CSVM -compile or ./CSVM.bin -compile if your on linux to compile the project.
