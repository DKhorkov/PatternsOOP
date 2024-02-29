
"""
Builder is a generative design pattern that allows to build complex objects step by step.
The builder makes it possible to use the same construction code to obtain different object representations.

Thanks to this pattern, the client can create objects by specifying only the necessary parameters,
which greatly simplifies the development process and eliminates the need to know all possible object configurations.

The Builder pattern proposes to move the construction of an object outside its own class,
entrusting this task to separate objects called builders.

The pattern suggests breaking down the process of constructing an object into separate steps
(for example, building Walls, inserting Doors, etc.). To create an object, client or director need to call
the builder's methods one by one. Moreover, there is no need to run all the steps,
but only those that are needed to produce an object of a certain configuration.

Often the same construction step may differ for different variations of manufactured objects.
For example, a wooden house will require the construction of walls made of wood, and a stone house - from stone.

In this case, it can be created multiple builder classes that perform the same steps in different ways.
By using these builders in the same construction process, client or director will be able to get a variety of outputs.
"""
