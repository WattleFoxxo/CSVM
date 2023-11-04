def CreateDll(name):
    """_summary_
    This function will create a dll file from a few templates
    """
    print("Creating project...")
   
        
    with open(f"{name}.csproj", "w") as file:
        file.write(f"""
                   <Project Sdk="Microsoft.NET.Sdk">
            <ItemGroup>
              <!-- .cs files -->

          <Reference Include="Home.dll" />
        </ItemGroup>

  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <ImplicitUsings>enable</ImplicitUsings>
    <Nullable>enable</Nullable>
  </PropertyGroup>

</Project>

                   """)
    with open(f"{name}.cusp", "w") as file:
        file.write(f"""using static Home;
                   
house {name} {{
    
    room stuff {{
        
        public struct function() {{
            
        }}
    }}
}}
""")
        with open("Project.cspm", "w") as file:
            file.write(
                f"""{name}""")
    print(f"Project {name} created! \n\n\n\n")
    print("You can run './CSVM -c' to compile your project")
    print("Or you can add the CVSM to your path and run it that way with -c")
    print("Please make sure that you have .NET 6.0 installed")
    print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
    print("And you have Home.dll in the same folder as the program")
    print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
    
def create_project(name):
    print("Creating project...")

    with open("{0}.csproj".format(name), "w") as file:
        file.write(
            f"""<Project Sdk="Microsoft.NET.Sdk">

                <ItemGroup>
                      <!-- .cs files -->
                  <Compile Include="{name}.cs" />
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
    with open(f"{name}.cusp", "w") as file:
        file.write('using static Home;\n\nPrint("Hello World!");')
    with open("Project.cspm", "w") as file:
        file.write(
            f"""{name}""")

        print("hello")
    print(f"Project {name} created! \n\n\n\n")
    print("You can run './CSVM -c' to compile your project")
    print("Or you can add the CVSM to your path and run it that way with -c")
    print("Please make sure that you have .NET 6.0 installed")
    print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
    print("And you have Home.dll in the same folder as the program")
    print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
    
    
    