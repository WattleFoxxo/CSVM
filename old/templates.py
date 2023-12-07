from token import AT


TokenTypes = {
    "KEYWORD": "KEYWORD",
    "IDENTIFIER": "IDENTIFIER",
    "NUMBER": "NUMBER",
    "STRING": "STRING",
    "OPERATOR": "OPERATOR",
    "COMMENT": "COMMENT",
    "NEWLINE": "NEWLINE",
    "EOF": "EOF",
    "ERROR": "ERROR",
    "NONE": "NONE",
    "LBRACE": "LBRACE",
    "RBRACE": "RBRACE",
    "LPAREN": "LPAREN",
    "RPAREN": "RPAREN",
    "LBRACKET": "LBRACKET",
    "RBRACKET": "RBRACKET",
    "SEMICOLON": "SEMICOLON",
    "COMMA": "COMMA",
    "DOT": "DOT",
    "COLON": "COLON",
    "DOLLAR": "DOLLAR",
    "AT": "AT",
    "AMPERSAND": "AMPERSAND",
    "CARET": "CARET",
    "TILDE": "TILDE",
    "PIPE": "PIPE",
    "QUESTION": "QUESTION",
    "EXCLAMATION": "EXCLAMATION",
    "NEW": "NEW",
    "IF": "IF",
    "ELSE": "ELSE",
    "WHILE": "WHILE",
    "FOR": "FOR",
    "SWITCH": "SWITCH",
    "CASE": "CASE",
    "DEFAULT": "DEFAULT",
    "BREAK": "BREAK",
    "CONTINUE": "CONTINUE",
    "RETURN": "RETURN",
    "STRUCT": "STRUCT", 
    "SWITCH": "SWITCH",
    "AT": "AT",
    "BLAND": "BLAND",
    "STOP": "STOP",
    "START": "START",
    "USING": "USING",
    "PUBLIC": "PUBLIC",
    "PRIVATE": "PRIVATE",
    "PROTECTED": "PROTECTED",
    "STATIC": "STATIC",
    "CLASS": "CLASS",
    "STRUCT": "STRUCT",
    "ENUM": "ENUM",
    "INTERFACE": "INTERFACE",
    "NAMESPACE": "NAMESPACE",
}


def CreateDll(name):
    """
    Creates a new project with the given name. 
    The project consists of a .csproj file, a .cusp file and a Project.cspm file.
    The .csproj file contains the project configuration and references to the Home.dll file.
    The .cusp file contains the project code.
    The Project.cspm file contains the name of the project.
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

</Project>""")
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
    print("You can run './CSVM -compile' to compile your project")
    print("Or you can add the CVSM to your path and run it that way with -c")
    print("Please make sure that you have .NET 6.0 installed")
    print("You can download it from https://dotnet.microsoft.com/download/dotnet/6.0")
    print("And you have Home.dll in the same folder as the program")
    print("you should have been given a copy of Home.dll with this program from the zip file you downloaded")
    
def create_project(name):
    """
    This function creates a new project with the given name. It creates a .csproj file, a .cusp file and a Project.cspm file.
    The .csproj file is a C# project file that can be used to build the project on Windows, Linux and Mac.
    The .cusp file is a C# script file that contains a simple "Hello World!" program.
    The Project.cspm file is a text file that contains the name of the project.
    """
    print("Creating project...")

    with open("{0}.csproj".format(name), "w") as file:
        file.write(
            f"""<Project Sdk="Microsoft.NET.Sdk">

                <ItemGroup>
                      <!-- .cs files -->
             
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
    
    
    