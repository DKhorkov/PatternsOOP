
"""
Lightweight is a structural design pattern that allows to fit more objects into the allocated RAM.
Lightweight saves memory by sharing the shared state of objects among themselves,
instead of storing the same data in each object.

The Lightweight pattern suggests not storing external state in a class, but passing it to certain
methods through parameters. This way, the same objects can be reused in different contexts.
But the main thing is that client needs much fewer objects, because now they will differ only in
their internal state, and this does not have many variations.
"""
