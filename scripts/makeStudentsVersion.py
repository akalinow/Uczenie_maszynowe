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
students_branch_name = branch_name.replace("_solutions","")
result = subprocess.run(["git", "checkout","-B" + students_branch_name], text=True, capture_output=True)
print(colored("Removing solutions blocks.","blue"))

fileList = glob.glob('./*.ipynb')
for aFile in fileList:
    input_file_name = aFile
    input_file_name = "01_Pakiety_numpy_pandas.ipynb"
    output_file = open("tmp.ipynb", "w")
    result = subprocess.run(["awk", " /#BEGIN_SOLUTION/{p=1}/#END_SOLUTION/{p=0;print \"    \\\"...\\\\n\\\", \";next}!p", input_file_name],
                            text=True, stdout=output_file)
    subprocess.run(["mv","tmp.ipynb",input_file_name])
    
print(colored("Commiting curent changes to students branch.","blue"))
subprocess.run(["git", "commit","-a", "-m automatic commit"])

print(colored("Switching back to solutions branch.","blue"))
subprocess.run(["git", "checkout",branch_name], text=True, capture_output=True)
