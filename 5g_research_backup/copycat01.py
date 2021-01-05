#!/usr/bin/env python3
# IMPORTS
import shutil
import os

# FORCE PYTHON TO 'START' IN HOME USER DIRECTORY
os.chdir("/home/student/mycode/")

# copy the file source to destination
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy a single file w/ shutil.copy() or an entire folder with all inside shutil.copytree()
shutil.copytree("5g_research/", "5g_research_backup/")

# the above has us back up our 5g research




