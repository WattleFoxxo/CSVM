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
CUSP 
"""
E3= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E4= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E5= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E6= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E7= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E8= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E9= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E10= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E11= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E12= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E13= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E14= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E15= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E16= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E17= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E18= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E19= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E20= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E21= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E22= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E23= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E24= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E25= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E26= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E27= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E28= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E29= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E30= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E31= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E32= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E33= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E34= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E35= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E36= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E37= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E38= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E39= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E40= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E41= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E42= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E43= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E44= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E45= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E46= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E47= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E48= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E49= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E50= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E51= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E52= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E53= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E54= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E55= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E56= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E57= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E58= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E59= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E60= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E61= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E62= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E63= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E64= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E65= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E66= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E67= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E68= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E69= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E70= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E71= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E72= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E73= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E74= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E75= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E76= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E77= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E78= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E79= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E80= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E81= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E82= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E83= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E84= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E85= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E86= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E87= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E88= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E89= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E90= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E91= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E92= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E93= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E94= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E95= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E96= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E97= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E98= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
"""
E99= """
# Lady Jessica

Bene Gesserit and concubine of Leto, and mother of Paul and Alia.
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

    def action_collapse_or_expand(self, collapse: bool) -> None:
        for child in self.walk_children(Collapsible):
            child.collapsed = collapse


if __name__ == "__main__":
    app = CollapsibleApp()
    app.run()
