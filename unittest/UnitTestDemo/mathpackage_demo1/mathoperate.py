#!/usr/bin/env python
# -*- coding: utf-8 -*-

import add
import minus
from multiply import multiply
from divide import devide

if __name__ == "__main__":
    print "2 + 3 = %d" % add.add(2, 3)
    print "5 - 2 = {}".format(minus.minus(5, 2))
    print "2 * 3 = {}".format(multiply(2, 3))
    print "8 / 4 = %d" % devide(8, 4)