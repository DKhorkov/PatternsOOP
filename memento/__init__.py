
"""
The Memento pattern assigns the creation of a copy of the object's state to the object itself, which owns this state.
Instead of getting internal objects state from outside, object will make a copy of his fields himself,
because all fields are available to him, even private ones.

The pattern suggests keeping a copy of the state in a special "snapshot" object with a limited interface that allows,
for example, to find out the date of manufacture or the name of the "snapshot". But, on the other hand, the "snapshot"
should be open to its creator for restoring purpose.

This scheme allows the creators to take "snapshots" and give them to other objects, called guardians, for storage.
The guardians will only have access to the limited interface of the "snapshot", so they will not be able to influence
the "insides" of the snapshot itself in any way. At the right moment, the guardian can ask the creator to restore
his condition by giving him the appropriate "snapshot".
"""
