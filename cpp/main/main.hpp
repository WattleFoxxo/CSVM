#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <QApplication>
#include <QMainWindow>
#include <QTextEdit>
#include <QMenuBar>
#include <string>

void print(const char* str)
{
    printf("%s\n", str);
}

void makewidgets()
{
    print("making widgets...");
    QTextEdit textedit;
    textedit.resize(640, 480);
    textedit.setWindowTitle("CubeScript Transpiler Console Window");
    textedit.show();
    QMenuBar menubar;
    menubar.resize(640, 480);
    menubar.setWindowTitle("CubeScript Transpiler Console Window");
    menubar.show();
}
