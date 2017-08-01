#!/usr/bin/python
# -*- coding: utf-8 -*-

# http://blog.csdn.net/suwei19870312/article/details/23258495/

#支持with语句的对象必须支持__enter__和__exit__方法
class WithSample:
    def __enter__(self):
        print "start __enter__ function!!!"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print "start __exit__ function!!!"
        print "__exit__::exc_type: ", exc_type
        print "__exit__::exc_val: ", exc_val
        print "__exit__::exc_trace: ", exc_tb

    def __str__(self):
        return "WithSample __str__ function!!!"

    def __repr__(self):
        return "WithSample __repr__ function!!!"

    def devide(self):
        val = 1 / 0
        return val

with open("test.log", "w") as file:
    for i in range(5):
        file.write(str(i))
        file.write("\n")

with open("test.log", "r") as file:
    for line in file.readlines():
        print line

with WithSample() as sample:
    print "WithSample: ", sample
    sample.devide()