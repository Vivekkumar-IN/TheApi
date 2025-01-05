TEST
====


This Script for testing some sphnix external or internal modules
---------------------------------------------------------------------



.. exec_code::
   :language: python
   :language_output: json
   :caption: Expected Output

   from TheApi import SaavnAPI

   # --- hide: start ---
   import asyncio

   async def m():
   # ---- hide: toggle ---
       print(await SaavnAPI().search("Fuck Millionaire")) 
   # --- hide: start ---
   asyncio.run(m())
   # --- hide: stop ---
