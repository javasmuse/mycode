#!/usr/bin/env python3
import shutil
import os

# force python to start in the home user directory
os.chdir("/home/student/mycode/")

# call on the shutil.move source to destination
shutil.move("raynor.obj", "ceph_storage/")

# this will overwrite if it already exists, so take care when using move

# prompt user for a new name for the kerrigan.obj fil
xname = input("What is the new name for kerrigan.obj? ")

# rename the file
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

