"""
A value object is a pattern that is necessary to protect the internal data of the original object
from changes from the outside.
Every time changes occur to the state of an object by interacting with the interface of this object,
a new object with a changed state is returned. Meanwhile, the original object remains unchanged.
The state of an object is set from the outside EXCLUSIVELY during initialization.
"""
