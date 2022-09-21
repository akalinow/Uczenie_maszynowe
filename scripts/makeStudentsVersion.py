#!/bin/python3

import os
import subprocess
import glob
from termcolor import colored



result = subprocess.run(["git", "branch","--show-current"], text=True, capture_output=True)
branch_name = result.stdout
branch_name = branch_name.rstrip("\n")

print(colored("Commiting curent changes to solution branch.","blue"))
subprocess.run(["git", "commit","-a", "-m automatic commit"])

print(colored("Switching to students branch.","blue"))
students_branch_name = branch_name.replace("_solution","")
result = subprocess.run(["git", "checkout ",students_branch_name], text=True, capture_output=True)

print(colored("Removing solutions blocks.","blue"))
fileList = glob.glob('./*.ipynb')

for aFile in fileList:
    input_name = aFile
    output_name = aFile
    result = subprocess.run(["awk", " /#BEGIN_SOLUTION/{p=1}/#END_SOLUTION/{p=0;print \"\\t\\\"...\\\\n\\\",\";next}!p", input_name, output_name], text=True, capture_output=True)

    
print(colored("Commiting curent changes to students branch.","blue"))
subprocess.run(["git", "commit","-a", "-m automatic commit"])

print(colored("Switching back to solutions branch.","blue"))
result = subprocess.run(["git", "checkout ",branch_name], text=True, capture_output=True)
