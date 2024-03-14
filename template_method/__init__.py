
"""
A template method is a behavioral design pattern that defines the skeleton of an algorithm,
shifting responsibility for some of its steps to subclasses.

Pattern suggests dividing the algorithm into a sequence of steps, describing these steps
in separate methods and calling them in one template method one after another.

This will allow subclasses to redefine some steps of the algorithm, leaving its structure and other steps that
are not so important for this subclass unchanged.

Situations when pattern is applicable:
1) When subclasses must extend the base algorithm without changing its structure.

The template method allows subclasses to extend certain steps of an algorithm through inheritance without
changing the structure of the algorithms declared in the base class.

2) When there are several classes doing the same thing with minor differences.

When editing one class, it is also necessary to make the same edits to other classes.

The template method pattern suggests creating a common superclass for similar classes and organizing the main
algorithm in it in the form of steps. Different steps can be overridden in subclasses.

This will eliminate duplication of code in several classes with similar behavior, but differing in details.
"""
