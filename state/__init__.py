
"""
State is a behavioral design pattern that allows objects to change behavior depending on their state.
From the outside, it appears that the class of the object has changed.

The State pattern suggests creating separate classes for each state that an object can be in, and then including
behaviors that correspond to these states.

Instead of storing the code for all the states, an initial object called a context will hold a reference to one
of the state objects and delegate state-specific work to it.

Thanks to the fact that state objects will have a common interface, the context will be able to delegate work to
the state without being tied to its class. The behavior of the context can be changed at any time by connecting
another state object to it.

Situations in which this pattern is applicable:
1) When an object whose behavior changes dramatically depending on its internal state, and there are many
types of states, and their code changes frequently.

The pattern suggests separating all fields and methods associated with certain states into their own classes.
The original object will constantly reference one of the state objects, delegating some of its work to it.
To change the state, it will be enough to substitute another state object into the context.

2) When the class code contains many large, similar conditional statements that select behaviors depending on
the current values of the class fields.

The pattern suggests moving each branch of such a conditional statement into its own class. All
the fields associated with this state can also be added here.

3) When a tabular method was deliberately used for implementing state machine, but are forced to put up with
code duplication for similar states and transitions.

The State pattern allows to implement a hierarchical state machine based on inheritance. Similar
states can be inherited from one parent class to avoid duplicating code.
"""
