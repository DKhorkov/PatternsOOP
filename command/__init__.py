
"""
A command is a behavioral design pattern that turns requests into objects,
allowing to pass them as arguments when calling methods, queue requests, log them,
and support the cancellation of operations.

The purpose of this pattern is to create a structure in which the sending class and the receiving class
are not directly dependent on each other.

Four terms are always associated with the Command template: commands (command), receiver of commands (receiver),
invoker of commands (invoker) and client (client). The Command object knows about the receiver and
calls the receiver method. The values of the receiver parameters are stored in the command.
The caller (invoker) knows how to execute the command and, possibly, makes a record of the executed commands.
The caller (invoker) knows nothing about the specific command, it only knows about the interface.
Both objects (the caller and several command objects) belong to the client object.
The client decides which commands to execute and when. To execute a command,
it passes the command object to the caller (invoker).

Using command objects makes it easier to build common components that need to be delegated or method calls
made at any time without having to know the methods of the class or method parameters.
Using the invoker allows to keep records of executed commands without the need for the client to know
about this accounting model (such accounting can be useful, for example,
to implement the cancellation and repetition of commands).
"""
