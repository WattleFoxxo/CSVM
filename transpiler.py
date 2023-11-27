import os
import subprocess
import sys
import time


import argparse
import ctypes
import re
from errors import *
import glob
import os
import glob
import subprocess




translation_dict = {
    'struct': ('static void'),
    'revoid': ('public static void'),
    'restring': ('public static string'),
    'reint': ('public static int'),
    'pubtask': ('public static async Task'),
    'pubbool': ('public static async bool'),
    'pubstring': ('public static async '),
    'pubint': ('public static async Task'),
    'pubfloat': ('public static async Task'),
    'pubchar': ('public static async Task'),
    'rehouse': ('public static namespace'),
    'refloat': ('public static float'),
    'rebool': ('public static bool'),
    'redictionary': ('public static Dictionary'),
    'relist': ('public static List'),
    'rearray': ('public static Array'),
    'reobject': ('public static object'),
    'rechar': ('public static char'),
    'rebyte': ('public static byte'),
    'reuint': ('public static uint'),
    'reulong': ('public static ulong'),
    'reshort': ('public static short'),
    'reushort': ('public static ushort'),
    'relong': ('public static long'),
    'redecimal': ('public static decimal'),
    'int': ('int'),
    'using Home;': ('using static Home;'),
    'house': (' namespace '),
    'float': (' float '),
    'bool': (' bool '),
    'if': (' if '),
    'else': (' else '),
    'room': ('class'),
    'while': (' while '),
    'for': (' foreach '),
    ' > ': (' in '),
    'void': (' void '),
    'return': (' return '),
    'stop': (' break '),
    'continue': (' continue '),
    'true': (' true '),
    'false': (' false '),
    'empty': (' null '),
    'this': (' this '),
    'base': (' base '),
    'bland': ('default'),
    'stop': ('break'),
    'at': ('case'),
    'using': ('using'),
    ';': (';'),
    '//': ('//')

}
keywords = [
    'struct',
    'revoid',
    'restring',
    'reint',
    'pubtask',
    'rehouse',
    'refloat',
    'rebool',
    'pubstring',
    'pubbool',
    'redictionary',
    'relist',
    'rearray',
    'reobject',
    'rechar',
    'rebyte',
    'reuint',
    'reulong',
    'reshort',
    'reushort',
    'relong',
    'redecimal',
    'public',
    'private',
    'protected',
    'static',
    'int',
    'house',
    'string',
    'float',
    'bool',
    'var',
    'if',
    'else',
    'room',
    'while',
    'for',
    'void',
    'return',
    'stop',
    'continue',
    'true',
    'false',
    'empty',
    'this',
    'base',
    'bland',
    'stop',
    'at',
    'using',
    'static',
    ';',
    'await',
    'catch',
    'Exception',
    '//',
    
]
def InvalidSystax(lnumber, error):
    """Prints the error and the line number

    Args:
        lnumber (var): the line number
        error (var): the error
    """
    print_errors(error + "\n" + lnumber)
    
    
    


def check_transpiled_code(non_transpiled_code, keywords, translation_dict):
    inside_string = False
    ignore_line = False
    for line in non_transpiled_code.split('\n'):
        if line.startswith('//'):
            ignore_line = True
        elif line.startswith("// "):
            ignore_line = True
        else:
            matches = re.findall(r'\b\w+\b', line)
            for word in matches:
                if word in keywords or word in translation_dict.keys():
                    ignore_line = True
                elif not ignore_line:
                    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', word):
                        raise SyntaxError(f"Invalid syntax CUSP 00003: Unknown keyword '{word}'")
        ignore_line = False
    return True

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    def __str__(self):
        return self.__repr__()
    def __eq__(self, other):
        return self.type == other.type and self.value == other.value
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        return hash(self.type) + hash(self.value)
    

class Tokens:
    
    # numbers
    NUMBERS = "0123456789"
    
    TT_INT = "INT"
    TT_STR = "STRING"
    TT_FLOAT = "FLOAT"
    TT_BOOL = "BOOL"
    TT_FOR = "FOR"
    TT_VAR = "VAR"
    TT_WHILE = "WHILE"
    TT_STOP = "STOP"
    TT_CONTINUE = "CONTINUE"
    TT_CRLBRKTLFT = "{"
    TT_CRLBRKTRTE = "}"
    TT_WAIT = "WAIT"
    TT_TRUE = "TRUE"
    TT_FALSE = "FALSE"
    TT_PUBLIC = "PUBLIC"
    TT_PRIVATE = "PRIVATE"
    TT_STATIC = "STATIC"
    TT_VOID ="VOID"
    TT_RDBRKTLFT = "("
    TT_RDBRKTRTE = ")"
    TT_IF = "IF"
    TT_ELSE = "ELSE"
    TT_CATCH = "CATCH"
    TT_AS = "AS"
    TT_IDENTIFIER = "IDENTIFIER"
    TT_EQUALS = "="
    TT_PLUS = "+"
    TT_MINUS = "-"
    TT_TIMES = "*"
    TT_DIVIDE = "/"
    TT_MODULO = "%"
    TT_POWER = "^"
    TT_DOT = "."
    TT_COMMA = ","
    TT_COLON = ":"
    TT_LSQBRACKET = "["
    TT_RSQBRACKET = "]"
    TT_AT = "@"
    TT_HASH = "#"
    TT_DOLLAR = "$"
    TT_TILDE = "~"
    TT_BACKTICK = "`"
    TT_NOT_EQUALS = "!="
    TT_GREATER_THAN = ">"
    TT_LESS_THAN = "<"
    TT_AND = "&&"
    TT_OR = "||"
    TT_NEWLINE = "\n"
    TT_EOF = "EOF"
    TT_ERROR = "ERROR"
    TT_COMMENT = "//"
    TT_COMMENT2 = "/*"
    TT_COMMENT3 = "*/"
    TT_COMMENT4 = "///"
    
    
# class Transpile:
#     # take in input text, seperate the lines, and only translate the words if the word is matching certan rules defined in the Transpile class
#     def __init__(self, text):
#         self.text = text
#         self.pos = -1
#         self.current_char = None
#         self.advance()

#     def make_number(self):
#         num_str = ""
#         dot_count = 0
#         while self.current_char != None and self.current_char in Tokens.NUMBERS + ".":
#             if self.current_char == ".":
#                 if dot_count == 1: break
#                 dot_count += 1
#                 num_str += "."
#             else:
#                 num_str += self.current_char
#             self.advance()
#         if dot_count == 0:
#             return Token(Tokens.TT_INT, int(num_str))
#         else:
#             return Token(Tokens.TT_FLOAT, float(num_str))
#     def make_identifier(self):
#         id_str = ""
#         while self.current_char != None and self.current_char in "abcdefghijklmnopqrstuvwxyz":
#             id_str += self.current_char
#             self.advance()
#         return Token(Tokens.TT_IDENTIFIER, id_str)
#     def make_string(self):
#         string = ""
#         self.advance()
#         while self.current_char != None and self.current_char != '"':
#             string += self.current_char
#             self.advance()
#         self.advance()
#         return Token(Tokens.TT_STR, string)
#     def make_plus(self):
#         self.advance()
#         return Token(Tokens.TT_PLUS)
#     def make_minus(self):
#         self.advance()
#         return Token(Tokens.TT_MINUS)
#     def make_times(self):
#         self.advance()
#         return Token(Tokens.TT_TIMES)
#     def make_divide(self):
#         self.advance()
#         return Token(Tokens.TT_DIVIDE)
#     def make_lparen(self):
#         self.advance()
#         return Token(Tokens.TT_RDBRKTLFT)
#     def make_rparen(self):
#         self.advance()
#         return Token(Tokens.TT_RDBRKTRTE)
#     def make_lbracket(self):
#         self.advance()
#         return Token(Tokens.TT_CRLBRKTLFT)
#     def make_rbracket(self):
#         self.advance()
#         return Token(Tokens.TT_CRLBRKTRTE)
#     def make_equals(self):
#         self.advance()
#         return Token(Tokens.TT_EQUALS)
#     def make_not_equals(self):
#         self.advance()
#         if self.current_char == "=":
#             self.advance()
#             return Token(Tokens.TT_NOT_EQUALS)
#         return Token(Tokens.TT_ERROR)
#     def make_greater_than(self):
#         self.advance()
#         if self.current_char == "=":
#             self.advance()
#             return Token(Tokens.TT_GREATER_THAN)
#         return Token(Tokens.TT_GREATER_THAN)
#     def make_less_than(self):
#         self.advance()
#         if self.current_char == "=":
#             self.advance()
#             return Token(Tokens.TT_LESS_THAN)
#         return Token(Tokens.TT_LESS_THAN)
#     def make_and(self):
#         self.advance()
#         if self.current_char == "&":
#             self.advance()
#             return Token(Tokens.TT_AND)
#         return Token(Tokens.TT_ERROR)
#     def make_or(self):
#         self.advance()
#         if self.current_char == "|":
#             self.advance()
#             return Token(Tokens.TT_OR)
#         return Token(Tokens.TT_ERROR)
#     def make_dot(self):
#         self.advance()
#         return Token(Tokens.TT_DOT)
#     def make_comma(self):
#         self.advance()
#         return Token(Tokens.TT_COMMA)
#     def make_colon(self):
#         self.advance()
#         return Token(Tokens.TT_COLON)
#     def make_lsqbracket(self):
#         self.advance()
#         return Token(Tokens.TT_LSQBRACKET)
#     def make_rsqbracket(self):
#         self.advance()
#         return Token(Tokens.TT_RSQBRACKET)
#     def make_modulo(self):
#         self.advance()
#         return Token(Tokens.TT_MODULO)
#     def make_power(self):
#         self.advance()
#         return Token(Tokens.TT_POWER)
#     def make_at(self):
#         self.advance()
#         return Token(Tokens.TT_AT)
#     def make_hash(self):
#         self.advance()
#         return Token(Tokens.TT_HASH)
#     def make_dollar(self):
#         self.advance()
#         return Token(Tokens.TT_DOLLAR)
#     def make_tilde(self):
#         self.advance()
#         return Token(Tokens.TT_TILDE)
#     def make_backtick(self):
#         self.advance()
#         return Token(Tokens.TT_BACKTICK)
#     def make_newline(self):
#         self.advance()
#         return Token(Tokens.TT_NEWLINE)
#     def make_eof(self):
#         self.advance()
#         return Token(Tokens.TT_EOF)
#     def make_error(self):
#         self.advance()
#         return Token(Tokens.TT_ERROR)
#     def make_comment(self):
#         self.advance()
#         return Token(Tokens.TT_COMMENT)
#     def make_comment2(self):
#         self.advance()
#         return Token(Tokens.TT_COMMENT2)
#     def make_comment3(self):
#         self.advance()
#         return Token(Tokens.TT_COMMENT3)
#     def make_comment4(self):
#         self.advance()
#         return Token(Tokens.TT_COMMENT4)
#     def make_for(self):
#         self.advance()
#         return Token(Tokens.TT_FOR)
#     def make_var(self):
#         self.advance()
#         return Token(Tokens.TT_VAR)
#     def make_while(self):
#         self.advance()
#         return Token(Tokens.TT_WHILE)
#     def make_stop(self):
#         self.advance()
#         return Token(Tokens.TT_STOP)
#     def make_continue(self):
#         self.advance()
#         return Token(Tokens.TT_CONTINUE)
#     def make_wait(self):
#         self.advance()
#         return Token(Tokens.TT_WAIT)
#     def make_true(self):
#         self.advance()
#         return Token(Tokens.TT_TRUE)
#     def make_forloop(self):
#         self.advance()
#         return Token(Tokens.TT_FORLOOP)
        
         
            
# class ParseResult:
#     def __init__(self):
#         self.error = None
#         self.node = None
#         self.advance_count = 0
#         self.to_reverse_count = 0
#     def register_advancement(self):
#         self.advance_count += 1
#     def register(self, res):
#         self.advance_count += res.advance_count
#         if res.error: self.error = res.error
#         return res.node
#     def try_register(self, res):
#         if res.error:
#             self.to_reverse_count = res.advance_count
#             return None
#         return self.register(res)
#     def success(self, node):
#         self.node = node
#         return self
#     def failure(self, error):
#         if not self.error or self.advance_count == 0:
#             self.error = error
#         return self
    
    
    





def transpile(event): # this is for transpiling
     """ Transpile the input text into C# code.
     Args:
         event (_str_): The input text to transpile.
     Returns:
         _str_: The transpiled C# code.
     """
     lines = event.splitlines()
     translated_lines = []
     # Apply translation line by line based on the dictionary
     for line in lines:
         # Split the line into words and punctuation marks
         words = re.split(r'(\W+)', line)
         translated_words = []
         try:
             check_transpiled_code(line, keywords,translation_dict)
         except Exception as e:
             print_errors(line, e)
         for word in words: # get the input text
             try:
                 # Convert word to lower case
                 lower_word = word.lower()
                 if lower_word in translation_dict:
                     # Preserve the original case of the word
                     if word[0].isupper():
                         translated_words.append(translation_dict[lower_word].capitalize())
                     else:
                         translated_words.append(translation_dict[lower_word])
                 else: #if the word is not in the dictionary
                     translated_words.append(word)
             except Exception as e:
                 print(f"Error translating word '{word}': {e}")
                 translated_words.append(word)
         translated_line = "".join(translated_words)
         translated_lines.append(translated_line)
     translated_text = "\n".join(translated_lines)
     return translated_text
    

def createoutput(translated_text): # this is for creating files
    """Create the output file.`

    Args:
        translated_text (_str_): returns the translated text
    """
    file_path = "Program.cs"
    with open(file_path, 'w') as file:
        file.write(translated_text)

def Compilee(file_name): 
    """
    Compile the input file.
    Args:
        file_name (_str_): The name of the file to compile.
    """
    file_path = file_name + ".cs"
    file_name = file_name + ".cusp"
    print(f"Compiling file '{file_name}'...")
    print(f"Transpiling file {file_path}")
    with open(file_name, 'r') as file:
        event = file.read()
    translated_text = transpile(event)
    with open(file_path, 'w') as file:
        file.write(translated_text)
    print("Compiling...")
  
    
        


def Compileprojectwithoutput():
    """instead of deleting the file like in the other compile project function, this one keeps the file and saves it to the output folder
    """

    # Read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()

    # Each line is a file with a .cusp extension. We need to transpile each one of them into a .cs file
    try:
        # Get the name of the .csproj file within the same directory
        current_directory = os.getcwd()

        # Find .csproj files in the current directory
        csproj_files = glob.glob(os.path.join(current_directory, "*.csproj"))

        # Get the first .csproj file name
        if csproj_files:
            csproj_file_name = os.path.basename(csproj_files[0])
            print(f".csproj file found: {csproj_file_name}")
        else:
            print_warning("No .csproj file found in the current directory.")
            exit()
    except Exception as e:
        print_error(f"Error finding .csproj file: {e}")
        exit()

    try:
        for line in filedata:
            # Get the file name
            file_name = line.strip()  # Remove newline characters
            print(f"Compiling file '{file_name}'...")

            # Open the file
            Compilee(file_name)

            # Check if the OS is Windows or not
           
                # If it is, use dotnet.exe
            subprocess.run(["dotnet build"])
            

            # Remove the .cs file * not available within --compout
            # os.remove(file_name + ".cs")

    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        


def Compileproject(): 
    """ compile the whole project.cspm file
    """
    #read the project file
    try:
        with open("Project.cspm", 'r') as file:
            filedata = file.readlines()  # readlines instead of read
    except Exception as e:
        print_error(f"CUSP 00001`: {e}")
        exit()
# each line is a file with a .cusp extension
# we need to transpile each one of them into a .cs file

    try:
        #get the name of the .csproj file within the same directory
       

        # get the current directory
        current_directory = os.getcwd()

        # find .csproj files in the current directory
        csproj_files = glob.glob(os.path.join(current_directory, "*.csproj"))




        # get the first .csproj file name
        if csproj_files:
            csproj_file_name = os.path.basename(csproj_files[0])
            print(f".csproj file found: {csproj_file_name}")
        else:
            print_error("No .csproj file found in the current directory.")
            exit()
    except Exception as e:
        print_error(f"Error finding .csproj file: {e}")
        exit()

    try:
        for line in filedata:
            # get the file name
            file_name = line.strip()  # remove newline characters
            print(f"Compiling file '{file_name}'...")
    except Exception as e:
        print_error(f"Error reading project file: {e}")
        exit()
    try:
        # open the file
        Compilee(file_name)
        
        #check if the os is windows or not
        
    except Exception as e:
        print_error(f"Error compiling file '{file_name}': {e}")
        
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False



def Runproject(name):
    """runs a project

    Args:
        name (_str_): the name of the cspm file
        
    """
    #read the project file
    with open(name + ".cspm", 'r') as file:
        filedata = file.read()
    # each line is a file with a .cusp extension
    # we need to transpile each one of them into a .cs file==
    
    for line in filedata:
        # get the file name
        file_name = line
        # open the file
        with open(file_name, 'r') as file:
            event = file.read()
        # transpile the file
        translated_text = transpile(event)
        # create the output file
        createoutput(translated_text)
        
        subprocess.run(["dotnet run"])
        
        
