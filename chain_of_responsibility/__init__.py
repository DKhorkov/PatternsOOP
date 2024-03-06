
"""
Chain of Responsibility is a behavioral design pattern that allows requests to be passed sequentially
through a chain of handlers. Each subsequent handler decides whether it can process the request itself and
whether it is worth passing the request further down the chain.

The pattern suggests linking handler objects into one chain. Each of them will have a link to the next
handler in the chain. Thus, when receiving a request, the handler will not only be able to do something with it,
but also transfer processing to the next object in the chain.

By passing requests to the first handler in the chain, client can be sure that all objects in the chain
will be able to process it. In this case, the length of the chain does not matter.

It is very important that all objects in the chain have a common interface.
Typically, each specific handler only needs to know that the next object in the chain has
a method "execute()." Thanks to this, the connections between chain objects will be more flexible.
In addition, client can form chains dynamically from a variety of objects, without being tied to specific classes.


Cases where the chain of responsibility can be applied:
1) When the program must process various requests in several ways, but it is not known in advance what specific
requests will come and what handlers will be needed for them.

With Chain of Responsibility, client can link potential handlers into one chain and, when a request is received,
ask each of them in turn if they would like to process the request.

2) When it is important that the handlers are executed one after another in a strict order.

The chain of responsibility allows client to run handlers sequentially one after another in the order in which
they appear in the chain.

3) When the set of objects capable of processing a request must be specified dynamically.

At any time, client can change existing chain and reassign connections between handlers in chain.
"""
