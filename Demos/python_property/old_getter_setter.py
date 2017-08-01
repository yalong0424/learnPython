#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person(object):
    """
    The Person class used to test attribute getter && setter functions, just like in java && C++.
    """
    def __init__(self):
        self.__name = ""
        self.__age = -1
        self.__sex = "female"

    def name(self):
        """
        The name attribute getter function.
        :return: name attribute.
        """
        return self.__name

    def setName(self, name):
        """
        The name attribute setter function.
        :param name: name
        :return: None
        """
        self.__name = name

    def age(self):
        """
        The age attribute getter function.
        :return: age attribute.
        """
        return self.__age

    def setAge(self, age):
        """
        The age attribute setter function.
        :param age: age
        :return: None
        """
        self.__age = age

    def sex(self):
        """
        The sex attribute getter function.
        :return: sex attribute.
        """
        return self.__sex

    def setSex(self, sex):
        """
        The sex attribute setter function.
        :param sex: sex
        :return: None
        """
        self.__sex = sex


def personTest():
    person = Person()
    print person.name()
    print person.age()
    print person.sex()

    person.setName("san zhang")
    person.setAge(20)
    person.setSex("male")

    print person.name()
    print person.age()
    print person.sex()

    #建议通过类名访问__doc__，使用对象访问，有时候会不准备，尤其是使用property时候
    print person.__doc__
    print Person.__doc__
    #use object.methodName.__doc__ style
    print person.name.__doc__
    print person.setName.__doc__
    print person.age.__doc__
    #use class.methodName.__doc__ style
    print Person.setAge.__doc__
    print Person.sex.__doc__
    print Person.setSex.__doc__


if __name__ == "__main__":
    personTest()