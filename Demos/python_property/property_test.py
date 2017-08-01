#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/functions.html#property

# property(fget=None, fset=None, fdel=None, doc=None)
#If c is an instance of C, c.x will invoke the getter, c.x = value will invoke the setter and del c.x the deleter.
#If given, doc will be the docstring of the property attribute. Otherwise, the property will copy fget‘s docstring (if it exists).

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

    def delName(self):
        """
        The name attribute deleter function.
        :return: None
        """
        del self.__name

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

    def delAge(self):
        """
        The age attribute deleter function.
        :return: None
        """
        del self.__age

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

    def delSex(self):
        """
        The sex attribute deleter function.
        :return: None
        """
        del self.__sex

    name = property(name, setName, delName, "I am the name attribute.")
    age = property(age, setAge, delAge) #没有设置docstring属性，则age的docstring默认读取其getter function的docstring
    sex = property(sex, None, delSex, "I am the sex attribute.") #声明sex属性为只读属性


def personTest():
    person = Person()

    #以下方法不可再调用了，换成通过声明的属性名称调用
    #print person.name()
    #print person.age()
    #print person.sex()

    print person.name
    print person.age
    print person.sex

    person.setName("san zhang")
    person.setAge(20)
    #在property() function中没有指定sex的setter function，但是类中存在sex的setter function的话，还是可以通过使用类中的setter function进行设置
    person.setSex("male")

    print person.name
    print person.age
    print person.sex

    person.name = "si li"
    person.age = 30
    #sex 是只读属性，因为没有为其设置 setter function
    #person.sex = "female"

    print person.name
    print person.age
    print person.sex

    del person.age
    del person.sex

    print person.name
    #删除的属性不能再次访问了
    #print person.age
    #print person.sex

    print Person.__doc__
    print Person.name.__doc__
    print Person.setName.__doc__
    print Person.delName.__doc__
    print Person.age.__doc__
    print Person.setAge.__doc__
    print Person.delAge.__doc__
    print Person.sex.__doc__
    print Person.setSex.__doc__
    print Person.delSex.__doc__


if __name__ == "__main__":
    personTest()