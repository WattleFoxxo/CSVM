#include "cubescript.hpp"

/// check Function for the CSVM
/// @param argc The number of arguments passed to the program
/// @param argv The arguments passed to the program
/// @return 0 if the check was successful, 1 if there was an error


int checkcsvm()
{
    // check if the Components are here

    std::cout << "Checking for CSVM Components..." << std::endl;

    // Get the current directory path
    std::filesystem::path currentPath = std::filesystem::current_path();

    // Specify the filenames to check
    std::vector<std::string> filenames = {"csvm", "addons/cstranspiler", "help"};

    // Check if each file exists in the current directory
    for (const std::string& filename : filenames)
    {
        std::filesystem::path filePath = currentPath / filename;
        if (std::filesystem::exists(filePath))
        {
            std::cout << "File " << filename << " exists!" << std::endl;
        }
        else
        {
            std::cout << "File " << filename << " does not exist!" << std::endl;
            return 1;
        }
    }

    return 0;
}


int main(int argc, char **argv)
{
    // start a check to see if all the CSVM components are here and if there are any addons aswell
    // if there are addons, load them

    // start the check

      if (checkcsvm() == 0)
      {
          std::cout << "CSVM is ready to use!" << std::endl;
          system("./compiler/csvm");
      }
      else
      {
          std::cout << "CSVM is not ready to use!" << std::endl;
      }

    return 0;
}
