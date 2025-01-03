Welcome to TheApix Documentation
===============================

Overview
--------

TheApix is designed to integrate multiple API keys and provide a unified interface for various functionalities. This documentation will guide you through the installation, configuration, and usage of TheApi.


.. attention ::

   This project is under active development. Expect frequent updates and improvements.


.. toctree::
   :hidden:
   :caption: Contents:

   client
   api/saavn/index



Installation
------------

To install TheApix, you can use pip:

.. code-block:: bash

   pip install TheApix

Usage
-----


.. important :: 

   All methods of the :obj:`~TheApi.Client` or :obj:`~TheApi.SaavnAPI` can be used asynchronously, allowing for non-blocking operations and improved performance in asynchronous environments.

To start using TheApix, follow these steps:

1. Import the Client module and initialize the client:

   .. code-block:: python

      from TheApi import Client

      api = Client()

2. Use the Client to make requests to the integrated APIs:

   .. code-block:: python

      response = await api.write("Radhe Radhe")

      print(response)

3. You can use the :obj:`~TheApi.SaavnAPI` for making request for endpoint of saavn.dev

   .. code-block:: python 

      from TheApi import SaavnAPI

      api = SaavnAPI()

      r = await api.search("Fuck Millionaire")
      
      print(r)