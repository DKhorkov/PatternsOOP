
"""
Visitor is a behavioral design pattern that allows new operations to be added to a program without
changing the object classes on which those operations can be performed.

Visitor pattern suggests placing new behavior in a separate class, rather than multiplying it across
multiple classes at once. The objects that the behavior was supposed to be associated with will pass themselves
to the visitor methods, instead of performing the behavior themselves.

Visitor can be used, when need to perform some unrelated operations on objects of a complex structure of objects,
but do not to “clog” the classes with such operations. Visitor allows to extract related
operations from the classes that make up the object structure by placing them in a single visitor class.
"""
