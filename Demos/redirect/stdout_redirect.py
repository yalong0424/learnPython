#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/lanbing510/article/details/8487997

import sys

print "Dive into python"
file = open("out.log", "w")
try:
    saveout = sys.stdout
    sys.stdout = file
    print "This message will be logged instead of display"
    sys.stdout = saveout
finally:
    file.close()
