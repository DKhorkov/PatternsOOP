from .abstract_prototype import AbstractPrototype
from .prototype_factory import PrototypeFactory

"""
The Prototype pattern entrusts the creation of copies to the objects being copied themselves. 
It introduces a common interface for all objects that support cloning. 
This allows to copy objects without being tied to their specific classes. 
Typically, such an interface has only one clone() method.

It allows to get away from implementation and to follow the principle of “programming through interfaces”. 
The returning type is the interface/abstract class at the top of the inheritance hierarchy.

Prototype - a pattern of creating an object by cloning another object instead of creating it through a constructor.
"""
