# Metaclasses - Simple Django Models
# Django is a famous back-end framework written in Python. It has a vast list of features including the creation of database tables
# through "models". You can see an example of such model below:
#
# class Person(models.Model):
#    first_name = models.CharField()
#    last_name = models.CharField()
# Apart from creating a table it can perform validation, generate HTML forms, and so on. This is possible thanks to metaclasses.
# Normally there are better solutions than using metaclasses, but they can be of great help in creating powerful framework interfaces.
# This goal of this kata is to learn and understand how such frameworks works.
#
# Your task is to implement a class Model and classes for its fields to support functionality like in the following example:
#
# class User(Model):
#    first_name = CharField(max_length=30)
#    last_name = CharField(max_length=50)
#    email = EmailField()
#    is_verified = BooleanField(default=False)
#    date_joined = DateTimeField(auto_now=True)
#    age = IntegerField(min_value=5, max_value=120, blank=True)
#
#
# user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
# user1.validate()
#
# print(user1.date_joined)  # prints date and time when the instance was created
# print(user1.is_verified)  # prints False (default value)
#
# user1.age = 256
# user1.validate()  # raises ValidationError - age is out of range
#
# user2 = User()
# user2.validate()  # raises ValidationError - first three fields are missing and mandatory
# The classes which inherit from Model should:
#
# support creation of fields using class-attribute syntax
# have a validate method which checks whether all fields are valid
# The field types you should implement are described below. Each of them also has parameters blank (default False),
# which determines whether None is allowed as a value, and default (default None) which determines the value to be used if nothing was
# provided at instantiation time of the Model.
#
# CharField - a string with min_length (default 0) and max_length (default None) parameters, both inclusive if defined
# IntegerField - an integer with min_value (default None) and max_value (default None) parameters, both inclusive if defined
# BooleanField - a boolean
# DateTimeField - a datetime with an extra parameter auto_now (default False). If auto_now is True and no default value has been provided,
# the current datetime should be used automatically at Model instantion time.
# EmailField - a string in the format of address@subdomain.domain where address, subdomain, and domain are sequences of alphabetical
# characters with min_length (default 0) and max_length (default None) parameters
# Each field type should have its own validate method which checks whether the provided value has the correct type and satisfies
# the length/value constraints.

from datetime import datetime
import re


class Field:
    def __init__(self, blank=False, default=None, *args, **kwargs):
        self.blank = blank
        self.default = default

    def validate(self, value):
        if self.blank and value is None:
            return

        if not self.blank and value is None and self.default is None:
            raise ValidationError("This field cannot be blank.")
        return


class ValidationError(Exception):
    pass


class CharField(Field):
    def __init__(
        self, min_length=0, max_length=None, blank=False, default=None, *args, **kwargs
    ):
        super().__init__(blank, default, *args, **kwargs)
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, value):
        if value is None and self.blank is True:
            return
        super().validate(value)

        if not isinstance(value, str):
            raise ValidationError("Value must be a string.")

        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(
                f"String is shorter than minimum length {self.min_length}."
            )

        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(
                f"String is longer than maximum length {self.max_length}."
            )


class IntegerField(Field):
    def __init__(
        self, blank=False, default=None, min_value=None, max_value=None, *args, **kwargs
    ):
        self.min_value = min_value
        self.max_value = max_value
        super().__init__(blank, default, *args, **kwargs)

    def validate(self, value):
        if value is None and self.blank is True:
            return
        super().validate(value)

        if not isinstance(value, int):
            raise ValidationError("Value must be a integer")

        if (self.min_value is not None and value < self.min_value) or (
            self.max_value is not None and value > self.max_value
        ):
            raise ValidationError(f"{value} is out of range")


class BooleanField(Field):
    def __init__(self, blank=False, default=None, *args, **kwargs):
        super().__init__(blank, default, *args, **kwargs)

    def validate(self, value):
     
        if value is None and self.blank is True:
            return
        super().validate(value)
        if value is not None and not isinstance(value, bool):
            raise ValidationError("Value is not a boolean value")


class DateTimeField(Field):
    def __init__(self, blank=False, default=None, auto_now=False, *args, **kwargs):
        self.auto_now = auto_now

        super().__init__(blank, default, *args, **kwargs)

    def validate(self, value):
        if value is None and self.blank is True:
            return
        super().validate(value)

        if not isinstance(value, datetime):
            raise ValidationError("Value must be a datetime object")


class EmailField(Field):
    def __init__(
        self,
        blank=False,
        default=None,
        min_length=0,
        max_length=None,
        *args,
        **kwargs,
    ):
        self.min_length = min_length
        self.max_length = max_length
        super().__init__(blank, default, *args, **kwargs)

    def validate(self, value):
        if value is None and self.blank:
            return
        super().validate(value)

        if isinstance(value, str) is False:
            raise ValidationError("Value must be a string")

        if not re.match("^[a-zA-Z]+@[a-zA-Z]+(\.[a-zA-Z]+)+$", value):
            raise ValidationError("Value is not an email")

        if self.min_length is not None and len(value) < self.min_length:
            raise ValidationError(
                f"String is shorter than minimum length {self.min_length}."
            )

        if self.max_length is not None and len(value) > self.max_length:
            raise ValidationError(
                f"String is longer than maximum length {self.max_length}."
            )


class AutoNowDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        attr_name = f"_{id(self)}_value"
        if not hasattr(instance, attr_name):
            setattr(instance, attr_name, datetime.now())
        return getattr(instance, attr_name)

    def __set__(self, instance, value):
        # Permite sobrescribir el valor si se asigna explícitamente
        attr_name = f"_{id(self)}_value"
        setattr(instance, attr_name, value)

class ModelMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}
        new_attrs = {}

        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
                if (
                    hasattr(value, "auto_now")
                    and value.auto_now
                    and value.default is None
                ):
                    new_attrs[key] = AutoNowDescriptor()
            else:
                new_attrs[key] = value

        new_attrs["_fields"] = fields

        def __init__(self, **kwargs):
          
            for field_name, field in self._fields.items():
                if hasattr(field, "auto_now") and field.auto_now and field.default is None:
                    continue
                
                if field_name in kwargs:
                    value = kwargs[field_name]
                elif field.default is not None:
                    value = field.default
                else:
                    value = None
               
                setattr(self, field_name, value)

        new_attrs["__init__"] = __init__

        def validate(self):
           
            for field_name, field in self._fields.items():
                value = getattr(self, field_name, None)
                
                field.validate(value)
          

        new_attrs["validate"] = validate

        return type.__new__(cls, name, bases, new_attrs)  
class Model(metaclass=ModelMeta):
    pass
