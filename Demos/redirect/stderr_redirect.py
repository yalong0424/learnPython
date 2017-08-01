#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/lanbing510/article/details/8487997

import sys

f = open("error.log", "w")
sys.stderr = f
raise Exception, "This exception msg will be logged"