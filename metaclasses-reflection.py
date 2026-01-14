# 1. Write a Python program to create a metaclass "UpperAttrMeta" that converts all attribute
# names of a class to uppercase.


from typing import Any, Dict


class UpperAttrMeta(type):
    def __new__(cls, name, bases, attrs):
        for key, value in dict(attrs).items():
            if not key.startswith("__"):
                attrs[key.upper()] = value
        return type.__new__(cls, name, bases, attrs)


class Test(metaclass=UpperAttrMeta):
    name = "test"
    age = 20


print(Test.NAME)
print(Test.AGE)


# 2. Write a Python program to create a metaclass "ValidateAttrMeta" that ensures all attributes
# of a class are integers. Raise a TypeError if any attribute is not an integer.


class ValidateAttrMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs_copy = attrs.copy()

        for key, value in attrs_copy.items():
            if not isinstance(value, int) or issubclass(type(value), int):
                print(f"Attribute {key} must be an integer")
        return type.__new__(cls, name, bases, attrs_copy)


class Test2(metaclass=ValidateAttrMeta):
    age = 20
    name = "test"

    def __init__(self, age, name) -> None:
        self.age = age
        self.name = name


test2 = Test2(age=20, name="test")
print(test2.age)
print(test2.name)


# 3. Write a Python program to create a metaclass SingletonMeta that ensures a
# class only has one instance (singleton pattern).


class SingletonMeta(type):
    singletons = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self.singletons:
            self.singletons[self] = super().__call__(*args, **kwds)
            print(f"Creating new instance of {self}")
        else:
            print(f"Returning existing instance of {self}")
        return self.singletons[self]


class Test3(metaclass=SingletonMeta):
    def __init__(self, name) -> None:
        self.name = name


test3_1 = Test3(name="test")
test3_2 = Test3(name="test")
print(test3_1)
print(test3_2)
print(test3_1 is test3_2)


# 4. Write a Python metaclass "AttrLoggingMeta" that logs every time an attribute is accessed or modified.


class AttrLoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs_copy = attrs.copy()

        for key, value in attrs_copy.items():
            if not key.startswith("__"):
                attrs[key] = cls.log_access(key, value)
        return super().__new__(cls, name, bases, attrs)

    @staticmethod
    def log_access(key: str, value: Any) -> Any:
        if callable(value):

            def wrapper(*args: Any, **kwargs: Any) -> Any:
                print(f"Calling method {key}")
                return value(*args, **kwargs)

            return wrapper
        else:
            return property(
                fget=lambda x: AttrLoggingMeta.log_read(key, value),
                fset=lambda x, y: AttrLoggingMeta.log_modification(key, value, x),
                fdel=lambda x: AttrLoggingMeta.log_deletion(key),
                doc=f"Property for {key}",
            )

    @staticmethod
    def log_modification(key: str, value: Any, instance: Any) -> Any:
        print(f"Modifying attribute {key}")
        instance.__dict__[key] = value
        return instance.__dict__[key]

    @staticmethod
    def log_deletion(key: str) -> Any:
        print(f"Deleting attribute {key}")
        return None

    @staticmethod
    def log_read(key: str, value: Any, instance: Any) -> Any:
        print(f"Reading attribute {key}")
        return instance.__dict__[key] or value


# 1. Write a Python function "create_class" that takes a class name and a dictionary of attributes and
# methods, and returns a dynamically created class with those attributes and methods.


def create_dynamic_class(future_name, future_base, future_attrs: Dict[Any, Any]):
    return type(future_name, future_base, future_attrs)


# 2. Write Python a function "add_method" that takes a class, a method name, and a method, and adds that method to the class.


def add_method(future_class, future_method_name, future_method):
    setattr(future_class, future_method_name, future_method)
    # return future_class
    # future_class.__dict__[future_method_name] = future_method

    # future_class.future_method_name = future_method
    return future_class


# 4. Write a Python function "create_inherited_class" that takes a base class, a class name, and a
# dictionary of additional attributes and methods, and returns a dynamically created subclass.


def create_inherited_class(future_base, future_name, future_attrs: Dict[Any, Any]):
    return type(future_name, (future_base,), future_attrs)


import re


def class_name_changer(cls, new_name: str):
    if not new_name[0].isupper():
        return Exception("Class name must start with an uppercase letter")

    # r'^[A-Z][a-zA-Z0-9]*$'a more exact regex
    if not re.match("^[A-Za-z0-9]+$", new_name):
        return Exception(
            "Class name must contain only alphanumeric characters and underscores"
        )

    cls.__name__ = new_name
    return cls


# def class_name_changer(cls, new_name: str):
#    assert new_name[0].isupper() and new_name.isalnum()
#    cls.__name__ = new_name


# - That name changing function is awesome! - Timmy heard from his boss - but would it not be possible to hide somehow that function in classes itself?
#
# Timmy was thinking about it for while than decided to contact with his guru - you - and ask about it. You offered him to build
# class that could be inherited, and could provide some class method to modify name of already existing classes. The new class
# should be named as
#
# ReNameAbleClass
# and the special one method should be
#
# change_class_name
# Like before, be sure that new solution will allow only names with alphanumeric chars (upper & lower letters plus digits),
# but starting only with upper case letter.
#
# Moreover, for testing purposes, he want new class to have
#
# __str__
# method which will be returning string like "Class name is: MyClass" for MyClass.


class ReNameAbleClass(object):
    @classmethod
    def change_class_name(cls, new_name):
        if not new_name[0].isupper() or not new_name.isalnum():
            raise ValueError(
                "Class name must start with an uppercase letter and contain only alphanumeric characters"
            )
        cls.__name__ = new_name

    @classmethod
    def __str__(cls):
        return f"Class name is: {cls.__name__}"


# - So!, shouted boss, heading to Tim's office, We have new contract!
# - What is it? - ask Tim.
# - Do not know, frankly, it's secret! It's from army! - boss was obviously excited.
# - So how are we supposed to write anything, if it is so big secret?
# - And that's the point! We won't know it, but we will write it. We have to prepare mechanism to create dynamic classes with propertie
# s and methods given as a parameters. - explained boss.
# - I don't think that's, umm... But would we at least know names of these properties and methods, right?
# - No. Remember that it's secret, so we'll not know anything!
# - Nah, it's impossible! - cried Tim.
#
# Then Tims went to find you - his almighty guru - and ask to help him. You reminded him:
# - It's Python, here everything is possible! Ok, let's see....
#
# So, in that Kata, your task is to finish function create_class that will get some class name and secret dictionary
# and make class of it. That dictionary will be delivered by function army_get_secret_from_file() which is already completed.
# Tim also asked you to make sure that if class name is empty, it should be None as result, and to make possible to call function
# without second parameter.
#
# Do not worry, these test properties and methods are dummy, so you won't know the army's mysteries, so you (probably) won't be executed.
#
#
#
# Check also previous: Python's Dynamic Classes #1 Kata and Python's Dynamic Classes #2 Kata.

def create_class(cls_name, secrets = {}):
    
    return type(cls_name, (), secrets)
