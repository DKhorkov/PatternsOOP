
"""
An adapter is a structural design pattern that allows objects with incompatible interfaces to work together.
This is a translator object that transforms the interface or data of one object into such a form that
it becomes understandable to another object.

In this case, the adapter wraps one of the objects, so that the other object does not even know about
the presence of the first one. For example, an object, that works in meters, could be wrapped with an adapter
that converts the data to feet.

Adapters can not only convert data from one format to another, but also help objects with different
interfaces work together. It works like this:

     1) The adapter has an interface that is compatible with one of the objects.
     2) Therefore, this object can freely call the adapter's methods.
     3) The adapter receives these calls and redirects them to the second object,
     but in the format and sequence that the second object understands.

Sometimes it is even possible to create a two-way adapter that works both ways.
"""
