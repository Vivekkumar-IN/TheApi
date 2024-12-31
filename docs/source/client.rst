Client
======

.. currentmodule:: TheApi


.. autoclass:: Client
   :exclude-members: __new__

.. code-block:: python
   
   from TheApi import Client
   
   api = Client()
   
   r = await api.write("Radhe Radh")
   
   print(r)