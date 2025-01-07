TEST
====


This Script for testing some sphnix external or internal modules
---------------------------------------------------------------------



.. exec_code::
   :linenos_output:
   :language_output: json
   :caption_output: Expected Output

   # hide: start
   from TheApi import SaavnAPI
   import json

   import asyncio

   async def m():

       h = await SaavnAPI().search("Fuck Millionaire")
       print(json.dumps(h))

   asyncio.run(m())
   # hide: stop
