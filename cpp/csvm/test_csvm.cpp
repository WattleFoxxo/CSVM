#include <cassert>
#include <iostream>
#include "csvm.cpp"
void test_checkcsvm()
{
    // Test case 1: All files exist
    // Set up the current directory path
    std::filesystem::path currentPath = "./";

    // Call the function
    int result = check();

    // Check the result
    assert(result == 0);
    std::cout << "Test case 1 passed!" << std::endl;

    // Test case 2: One file does not exist
    // Set up the current directory path
    currentPath = "/d:/postreset/repos/CSVM/cpp/csvm";

    // Remove one file
    std::filesystem::remove(currentPath / "csvm");

    // Call the function
    result = check();

    // Check the result
    assert(result == 1);
    std::cout << "Test case 2 passed!" << std::endl;

    // Test case 3: All files do not exist
    // Set up the current directory path
    currentPath = "/d:/postreset/repos/CSVM/cpp/csvm";

    // Remove all files
    std::filesystem::remove(currentPath / "csvm");
    std::filesystem::remove(currentPath / "addons/cstranspiler");
    std::filesystem::remove(currentPath / "help");

    // Call the function
    result = check();

    // Check the result
    assert(result == 1);
    std::cout << "Test case 3 passed!" << std::endl;
}

int main()
{
    test_checkcsvm();

    return 0;
}