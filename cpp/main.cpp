
#include "main.hpp"

// CubeScript Transpiler Console Window
// (c) 2023 by OpenStudioCorporation
// developers and contributors

// This is the main file for the CubeScript Transpiler Console Window.

void printwelcome()
{
    print("welcome to the official CubeScript Transpiler!");
}


int main(int argc, char** argv)
{
    printwelcome();
    print("making window...");
    QApplication app(argc, argv);
    QMainWindow window;
    window.resize(640, 480);
    window.setWindowTitle("CubeScript Transpiler Console Window");
    makewidgets();
    window.show();
    return app.exec();
    return 0;
}


void runprojectcreator()
{
    print("running project creator...");
    system("./projectcreator");
}
