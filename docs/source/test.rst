TEST
====


This Script for testing some sphnix external or internal modules
---------------------------------------------------------------------



.. exec_code::

   print('Easy!')


.. exec_code::
  
   from TheApi import SaavnAPI

   import asyncio

   async def m():
       print(await SaavnAPI().search("Fuck Millionaire")) 
   asyncio.run(m())

