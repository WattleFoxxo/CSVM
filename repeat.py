import os
import re
import sys
import argparse

    # take the template E{Number} and replace it with the number

template = "E{Number}"

def replace_template(template, number):
    # replace the template with the number
    return template.replace("E{Number}", str(number))

# replace the number with 1 thru 100

for i in range(1, 100):
    print( "E"+replace_template(template, i))
    
    
        