
"""
An iterator is a behavioral design pattern that makes possible to sequentially traverse the elements of composite
objects without revealing their internal representation.

The idea behind the Iterator pattern is to take the collection traversal behavior out of the collection itself and
paste it into a separate class.

The iterator object will keep track of the traversal state, the current position in the collection,
and how many elements remain to be traversed. Different iterators will be able to traverse the same collection
at the same time, and the collection itself will not even know about it.

Plus, if needed to add a new traversal, a new iterator class can be created without changing
the existing collection code.
"""
