"""
This module contains a CollapsibleApp class that displays help documentation for CubeScript.
The class has a method to collapse or expand all sections and a collapsible container for the "How to get started" section.
"""
from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Footer, Label, Markdown

HowToGetStarted = """\
# How to get started with CubeScript

Welcome to the official CubeScript documentation!

this is a work in progress, so please be patient.

In order to get started with CubeScript.

just run the program and type 'new' to create a new project.

please report any errors to the github page.

https://github.com/charlie-sans/CVSM-Repo/issues


"""
Errors = """
# Errors? what do you mean i have errors?

Sometimes you will get errors, this is normal.

within this section we will go over the errors you may encounter.

Clicking on any of the blue rectangles that have the matching error code will take you to the section of the documentation that explains the error.

you can also press 'c' to collapse all sections and 'e' to expand all sections.

"""

E1= """
CUSP 00001: the file does not exist

This error means that the file you are trying to compile does not exist.

it could be ether that you typed the file name wrong or that the file does not exist.

try recompiling the file and if that does not work, try creating a new project.
"""
E2= """
CUSP 00002 invalid arguments

This error means that you have passed invalid arguments to the transpiler.

dont worry, i do the same when i work on CSVM


"""
E3= """
# CUSP 0003 Invalid syntax

from version 1.3 CubeScript now implements a syntax Checker for you error hungry nerds

this error means that you have invalid syntax in your code.

this could be caused by a typo in your code or a missing semicolon.
 
should print out a error somewhere in the console that you ran CSVM in so thats a great start.


"""
E4 = """
CUSP 00004: Invalid function arguments

This error means that you have passed invalid arguments to a function. 

Check the function definition to ensure that you are passing the correct number and type of arguments.
"""

E5 = """
CUSP 00005: Undefined variable

This error means that you are trying to use a variable that has not been defined.

Make sure that you have spelled the variable name correctly and that it has been defined before you try to use it.
"""

E6 = """
CUSP 00006: Type error

This error means that you are trying to perform an operation on a value of the wrong type.

For example, you might be trying to add a string to an integer, which is not allowed. Check the types of your values to make sure they are correct.
"""
E7= """
# CUSP 00007 
"""


class CollapsibleApp(App[None]):
    """help window"""

    BINDINGS = [
        ("c", "collapse_or_expand(True)", "Collapse All"),
        ("e", "collapse_or_expand(False)", "Expand All"),
    ]

    def compose(self) -> ComposeResult:
        """Compose app with collapsible containers."""
        yield Footer()
        
        with Collapsible(collapsed=True, title="How to get started"):
            yield Label(HowToGetStarted)
        with Collapsible(collapsed=True, title="Cusp 00001"):
            yield Label(E1)
        with Collapsible(collapsed=True, title="Cusp 00002"):
            yield Label(E2)
        with Collapsible(collapsed=True, title="Cusp 00003"):
            yield Label(E3)
        with Collapsible(collapsed=True, title="Cusp 00004"):
            yield Label(E4)
        with Collapsible(collapsed=True, title="Cusp 00005"):
            yield Label(E5)
        with Collapsible(collapsed=True, title="Cusp 00006"):
            yield Label(E6)
        with Collapsible(collapsed=True, title="Cusp 00007"):
            yield Label(E7)
        with Collapsible(collapsed=True, title="Errors"):
            yield Label(Errors)
        yield Markdown(
            """
            # How to get started with CubeScript

            Welcome to the official CubeScript documentation!
            
            i'm charlie-san, and i'm here to help explain anything you may need!

            this is a work in progress, so please be patient.

            In order to get started with CubeScript.

            just run the program and type 'new' to create a new project.

            please report any errors to the github page.
            
            """)

    def action_collapse_or_expand(self, collapse: bool) -> None:
        for child in self.walk_children(Collapsible):
            child.collapsed = collapse


if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
