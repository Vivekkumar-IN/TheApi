TEST
====


This Script for testing some sphnix external or internal modules
---------------------------------------------------------------------



.. exec_code::
   :language: python
   :caption: Expected Output

   # hide: start
   from TheApi import SaavnAPI

   import asyncio

   async def m():

       print(await SaavnAPI().search("Fuck Millionaire")) 
   asyncio.run(m())
   # hide: stop
