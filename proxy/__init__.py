
"""
A proxy is a structural design pattern that allows to substitute special proxy objects instead of real objects.
These objects intercept calls to the original object, allowing something to be done before or after the call
is passed to the original.

Common uses of a proxy:
1) Lazy initialization (virtual proxy). When you have a heavy object loading data from the file system or database.
Instead of loading data immediately after the program starts, proxy saves resources and create an object when it
really needed to be used.

2) Access protection (protective proxy). When a program has different types of clients and it's needed to
protect an object from unauthorized access. For example, if objects are an important part of the operating system,
and clients are third-party programs (good or malicious).
The proxy can check access on each call and pass execution to a service object if access is allowed.

3) Local launch of the service (remote proxy). When the real service object is located on a remote server.
In this case, the proxy translates client requests into calls over the network in a protocol that the remote
service can understand.

4) Logging requests (logging proxy). When it's needed to store the history of calls to a service object.
The proxy can save the history of the client's access to the service object.

5) Object caching (“smart” link). When it's needed to cache the results of client requests and manage their lifecycle.
The proxy can count the number of service object references that have been issued to the client and remain active.
When all references are released, it will be possible to release the service object itself
(for example, close the connection to the database).
In addition, the Deputy can track whether the client has changed the service object.
This will allow to reuse objects and save a lot of resources, especially when it comes to large, power-hungry services.
"""
