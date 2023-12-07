# Module Overview
"""
This module defines the CollapsibleApp class, providing a comprehensive help documentation interface for CubeScript users.
The class offers methods to efficiently collapse or expand all sections, enhancing user experience.
Additionally, it incorporates a collapsible container specifically dedicated to guiding users on how to get started.
"""

from textual.app import App, ComposeResult
from textual.widgets import Collapsible, Footer, Label, Markdown

# How to Get Started Section
HowToGetStarted = """
# Getting Started with CubeScript

Welcome to the official CubeScript documentation!

This documentation is an ongoing project, and we appreciate your patience.

To initiate your CubeScript journey:
1. Run the program.
2. Type 'new' to create a new project.

If you encounter any issues, kindly report them on our GitHub page:
[CubeScript GitHub Issues](https://github.com/charlie-sans/CVSM-Repo/issues)
"""

# Error Handling Section
Errors = """
# Encounter an Error?

Errors are a natural part of the process. In this section, we address common errors you may encounter. Click on the blue rectangles with matching error codes for detailed explanations.

You can also use 'c' to collapse all sections and 'e' to expand all sections.
"""

# Error Descriptions
E1 = """
CUSP 00001: File Not Found

This error signifies that the file you are attempting to compile does not exist. Double-check the file name for typos or verify its existence. If issues persist, consider creating a new project.
"""

E2 = """
CUSP 00002: Invalid Arguments

This error occurs when invalid arguments are provided to the transpiler. Ensure proper argument usage for a seamless experience.
"""

E3 = """
CUSP 00003: Invalid Syntax

With the introduction of syntax checking in CubeScript version 1.3, this error indicates invalid syntax in your code. Check for typos or missing semicolons and refer to the console output for specific error details.
"""

E4 = """
CUSP 00004: Invalid Function Arguments

This error arises when invalid arguments are passed to a function. Refer to the function definition to confirm the correct number and types of arguments.
"""

E5 = """
CUSP 00005: Undefined Variable

This error indicates an attempt to use an undefined variable. Ensure correct spelling and prior definition of the variable before usage.
"""

E6 = """
CUSP 00006: Type Error

When performing operations on values of incorrect types, this error is triggered. Verify the types of your values to maintain consistency.
"""

E7 = """
CUSP 00007: Missing Braces

This error suggests a likely absence of curly braces at the beginning or end of your code block. Verify that all code blocks have proper curly brace placement.
"""

E8 = """
CUSP 00008: Duplicate Function Definition

This error warns against defining a function with a duplicate name within the same scope. Each function must have a unique name to avoid conflicts.
"""

E9 = """
CUSP 00009: Unexpected End of File

Unexpectedly reaching the end of the file may be due to a missing closing brace or an incomplete statement. Review your code for proper brace placement and statement completion.
"""

E10 = """
CUSP 00010: Unsupported Feature

Encountering this error indicates usage of a feature not yet supported by the CubeScript transpiler. Refer to the documentation for supported features or anticipate updates with desired functionalities.
"""

E11 = """
CUSP 00011: Infinite Loop Detected

This error is triggered when an infinite loop is detected in your code. Prevent program crashes and excessive resource consumption by ensuring proper exit conditions in your loop.
"""

E12 = """
CUSP 00012: File Access Denied

When the transpiler attempts file access without the necessary permissions, this error occurs. Confirm that the transpiler has appropriate read and write permissions for the specified files and directories.
"""

E13 = """
CUSP 00013: Module Not Found

This error signifies the inability to find a required module or library. Review import statements and verify that specified modules are correctly installed and accessible.
"""

E14 = """
CUSP 00014: Stack Overflow

Exceeding the transpiler's call stack capacity results in this error. Prevent stack overflow by ensuring proper termination conditions in your recursive functions.
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
    with Collapsible(collapsed=True, title="Cusp 00008"):
        yield Label(E8)
    with Collapsible(collapsed=True, title="Cusp 00009"):
        yield Label(E9)
    with Collapsible(collapsed=True, title="Cusp 00010"):
        yield Label(E10)
    with Collapsible(collapsed=True, title="Cusp 00011"):
        yield Label(E11)
    with Collapsible(collapsed=True, title="Cusp 00012"):
        yield Label(E12)
    with Collapsible(collapsed=True, title="Cusp 00013"):
        yield Label(E13)
    with Collapsible(collapsed=True, title="Cusp 00014"):
        yield Label(E14)
    with Collapsible(collapsed=True, title="Errors"):
        yield Label(Errors)
    yield Markdown(
        """
        # How to get started with CubeScript

        Welcome to the official CubeScript documentation!
        
        I'm charlie-san, and I'm here to help explain anything you may need!

        This is a work in progress, so please be patient.

        In order to get started with CubeScript:

        1. Run the program.
        2. Type 'new' to create a new project.

        Please report any errors to the GitHub page.
        
        """)


    def action_collapse_or_expand(self, collapse: bool) -> None:
        for child in self.walk_children(Collapsible):
            child.collapsed = collapse


if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
