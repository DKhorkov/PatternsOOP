
"""
A mediator is a behavioral design pattern that allows to reduce the coupling of multiple classes among
themselves by moving these connections into a single mediator class.

The Mediator pattern forces objects to communicate not directly with each other, but through a separate mediator
object that knows to whom a particular request needs to be forwarded. Thanks to this, the system components will
depend only on the intermediary, and not on dozens of other components.

Examples of using the pattern:

1) When it is difficult to change some classes due to the fact that they have many chaotic connections
with other classes.

The mediator allows to put all these relationships into one class, after which it will be easier to
refactor them, make them more understandable and flexible.

2) When a class can't be reused because it depends on a lot of other classes.

After applying the pattern, the components lose their previous connections with other components,
and all their communication occurs indirectly, through an intermediary object.

3) When many subclasses of components should be created to use the same components in different contexts.

If previously a change in relationships in one component could lead to an avalanche of changes in all other components,
now client just need to create a mediator subclass and change the relationships between components in it.

In our example, we used the Engine class and the Ignition class in two completely different abstractions
(Car and Chainsaw) without directly linking these classes to each other.
"""
