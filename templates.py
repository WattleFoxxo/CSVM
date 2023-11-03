def CreateDll():
    """_summary_
    This function will create a dll file from a few templates
    """
    print("Creating project...")
    name = input("What do you want to name your project? ")

        
    with open(f"{name}.csproj", "w") as file:
        file.write("""
                   <Project Sdk="Microsoft.NET.Sdk">

  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>

                   """)
    with open(f"{name}.cusp", "w") as file:
        file.write(f""" using static Home;""")
    print(f"Project {name} created! \n\n\n\n")
    print("You can run './cusp compile' to compile your project")
    print("Or you can add the CVSM to your path")
    print("Please make sure that you have .NET 6.0 installed")
    print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
    print("And you have Home.dll in the same folder as the program")
    print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
    
def create_project(name):
    print("Creating project...")
    with open("Program.cs", "w") as file:
        file.write("")
    with open("{0}.csproj".format(name), "w") as file:
        file.write(
            """<Project Sdk="Microsoft.NET.Sdk">

                <ItemGroup>
                      <!-- .cs files -->
                  <Compile Include="program.cs" />
                  <Reference Include="System" />
                  <Reference Include="Home.dll" />
                </ItemGroup>

                <PropertyGroup>
                  <OutputType>Exe</OutputType>
                  <TargetFramework>net6.0</TargetFramework>
                  <ImplicitUsings>enable</ImplicitUsings>
                  <Nullable>enable</Nullable>
                </PropertyGroup>

                </Project>
"""
        )
    with open("Program.cusp", "w") as file:
        file.write('using static Home;\n\nPrint("Hello World!");')
    with open(f"{name}.cspm", "w") as file:
        file.write(
            """<HEAD>
<version>1.2</version>
    <encoding>UTF-8</encoding>
    <stagingArea>
    <Library>Home</Library>
    <Library>System</Library>
    </stagingArea>
</HEAD>
"""
        )

        print("hello")
    print(f"Project {name} created! \n\n\n\n")
    print("You can run './cusp compile' to compile your project")
    print("Or you can add the CVSM to your path")
    print("Please make sure that you have .NET 6.0 installed")
    print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
    print("And you have Home.dll in the same folder as the program")
    print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
    
    
    