#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/functions.html#property

# 使用 @property @attr.setter @attr.deleter 修饰器声明属性

class Person(object):
    """
    The Person class used to test attribute getter && setter functions, just like in java && C++.
    """
    def __init__(self):
        self.__name = ""
        self.__age = -1
        self.__sex = "female"

    #name是具有读写和删除权利的属性
    @property
    def name(self):
        """
        The name attribute getter function.
        :return: name attribute.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        The name attribute setter function.
        :param name: name
        :return: None
        """
        self.__name = name

    @name.deleter
    def name(self):
        """
        The name attribute deleter function.
        :return: None
        """
        del self.__name

    #age是只读属性，但可删除
    @property
    def age(self):
        """
        The age attribute getter function.
        :return: age attribute.
        """
        return self.__age

    @age.deleter
    def age(self):
        """
        The age attribute deleter function.
        :return: None
        """
        del self.__age

    #sex属性可读写，但是不可删除
    @property
    def sex(self):
        """
        The sex attribute getter function.
        :return: sex attribute.
        """
        return self.__sex

    @sex.setter
    def sex(self, sex):
        """
        The sex attribute setter function.
        :param sex: sex
        :return: None
        """
        self.__sex = sex

def personTest():
    person = Person()

    #以下方法不可再调用了，换成通过声明的属性名称调用
    #print person.name()
    #print person.age()
    #print person.sex()

    print person.name
    print person.age
    print person.sex

    person.name = "si li"
    # age 是只读属性，因为没有为其设置 setter function
    #person.age = 30
    person.sex = "male"

    print person.name
    print person.age
    print person.sex

    del person.name
    del person.age
    # sex属性不支持删除操作，因为没有为其设置deleter function
    #del person.sex

    # 删除的属性不能再次访问了
    #print person.name
    #print person.age
    print person.sex

    print Person.__doc__
    #获取@property声明的属性的docstring，获取的是其getter function的docstring
    print Person.name.__doc__
    print Person.age.__doc__
    print Person.sex.__doc__


if __name__ == "__main__":
    personTest()