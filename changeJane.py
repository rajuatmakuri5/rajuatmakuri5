#!/usr/bin/env python3

import sys
import subprocess

with open (sys.argv[1], "r") as newfile:
 path = '/home/student-0xxxxxxxxx'
 for line in newfile.readlines():
  newline = line.strip()   #it removes an whitespace, newline characters
  #print (newline)
  newtext = newline.replace("jane", "jdoe")  #search for the string jane and replace it with jdoe
  #print (newtext)
  subprocess.run(['mv', path+newline, path+newtext])
newfile.close()
