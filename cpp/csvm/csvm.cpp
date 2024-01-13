#include <string>
#include "cubescript.hpp"
#include <cstdlib>
/// check Function for the CSVM
/// @param argc The number of arguments passed to the program
/// @param argv The arguments passed to the program
/// @return 0 if the check was successful, 1 if there was an error



#pragma region check
int check()
{
    // check if the Components are here

    std::cout << "Checking for CSVM Components..." << std::endl;

    // Get the current directory path
    std::filesystem::path currentPath = std::filesystem::current_path();

    // Specify the filenames to check
    std::vector<std::string> filenames = {"csvm", "addons/cstranspiler", "help", "updater"};

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

    // Check if the addons directory exists
    std::filesystem::path addonsPath = currentPath / "addons";
    if (std::filesystem::exists(addonsPath))
    {
        std::cout << "Directory addons exists!" << std::endl;
        // check if anything is within the directory
        std::filesystem::directory_iterator addonsDir(addonsPath);
        if (addonsDir == std::filesystem::directory_iterator())
        {
            std::cout << "Directory addons is empty!" << std::endl;
        }
        else
        {
            std::cout << "Directory addons is not empty!" << std::endl;
            // check if the addons are there
            std::vector<std::string> addons = {"cstranspiler"};
            for (const std::string& addon : addons)
            {
                std::filesystem::path addonPath = addonsPath / addon;
                if (std::filesystem::exists(addonPath))
                {
                    std::cout << "Addon " << addon << " exists!" << std::endl;
                }
                else
                {
                    std::cout << "Addon " << addon << " does not exist!" << std::endl;
                    return 1;
                }
            }
        }
    }
    else
    {
        std::cout << "Directory addons does not exist!" << std::endl;
        return 1;
    }


    return 0;
}
#pragma endregion check






int main(int argc, char **argv)
{
    // start a check to see if all the CSVM components are here and if there are any addons aswell
    // if there are addons, load them

    // start the check



    if (check() == 0)
    {
        
        std::string OS = get_os(); // Remove the namespace qualifier
        if (OS == "Windows")
        {
            std::cout << "You are running Windows!" << std::endl;
            system("./csvm");
        }
        else if (OS == "Unix")
        {
            std::cout << "You are running Unix!" << std::endl;
            system("./csvm");
        }
        else if (OS == "Mac OSX")
        {
            std::cout << "You are running Mac OSX!" << std::endl;
            system("./csvm");
        }
        else if (OS == "Linux")
        {
            std::cout << "You are running Linux!" << std::endl;
            system("./csvm");
        }
        else if (OS == "FreeBSD")
        {
            std::cout << "You are running FreeBSD!" << std::endl;
            system("./csvm");
        }
        else
        {
            std::cout << "You are running an unknown OS?" << std::endl;
            std::cout << "Please report this to the CSVM developers!" << std::endl;
            std::cout << "You can still try to run CSVM!" << std::endl; 
            system("./csvm");
        }
        std::cout << "CSVM is ready to use!" << std::endl;
    }
    
    else
    {
        std::cout << "CSVM is not ready to use!" << std::endl;
    }



    return 0;
}


std::string get_os()
{
    #ifdef _WIN32
        return "Windows";
    #elif _WIN64
        return "Windows";
    #elif __unix || __unix__
        return "Unix";
    #elif __APPLE__ || __MACH__
        return "Mac OSX";
    #elif __linux__
        return "Linux";
    #elif __FreeBSD__
        return "FreeBSD";
    #else
        return "Other";
    #endif
}
