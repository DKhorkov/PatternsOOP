
"""
An observer is a behavioral design pattern that creates a subscription mechanism that allows one object
to monitor and respond to events occurring in other objects.

The Observer pattern suggests storing a list of references to subscriber objects inside the publisher object,
without the publisher having to maintain the subscription list itself. It will provide methods by which subscribers
can add or remove themselves from the list.

Applies in the following cases:
1) When, after changing the state of one object, something should also be done in others, but it is not known
which ones specifically, as well as their count.

The Observer pattern allows any object with a subscriber interface to register to receive notifications about
events occurring in publisher objects.

2) When some objects must observe others, but only in certain cases.

Publishers maintain dynamic lists. All observers can subscribe or unsubscribe from receiving alerts while the program
is running.
"""
