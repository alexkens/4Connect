4Connect Project
========

project will solve your problem of where to start with documentation,
by providing a basic explanation of how to do it easily.

Look how easy it is to use:

    import project
    # Get your stuff done
    project.do_stuff()

Features
--------

- Be awesome
- Make things faster

Installation
------------

Install $project by running:

    install project

Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@google-groups.com

License
-------

The project is licensed under the BSD license.

RidePooling
===========

Fleet simulation that generates a schedule out of ride requests.

Get started
-----------

You can clone the current repository of RidePooling to your local machine using HTTPS:

.. code:: bash

    git clone https://github.com/marcusschober/ridepooling.git

Or SSH:

.. code:: bash

    git clone git@github.com:marcusschober/ridepooling.git

Setting up an environment
-------------------------

With Virtual env
~~~~~~~~~~~~~~~~

| Create a new virtual environment (for example in PyCharm or via the command line ``python3 -m venv venv``). Activate it with:
| Terminal:  ``source venv/bin/activate``
| Windows: ``venv\Scripts\activate``
| Note: You need to be in the project folder to activate the environment
|
| Install the requirements with ``pip install -e .``

| Note: PyCharm might tell you that it can't find the main module.
| In that case you have to right click the folder "src" and select
| "Mark Directory as" -> "Sources Root"

With Poetry
~~~~~~~~~~~

| First install Poetry

.. code:: bash

    pip install poetry

| Then initialize the virtual environment for Poetry. It will be stored it in the
cache directory, and display a randomly generated name for the virtual environment.

.. code:: bash

    poetry env use python

or on Windows

.. code:: bash

    poetry env use py

| Poetry also installs any dependencies listed in the project’s pyproject.toml file.


Running the program
-------------------

To run this from the command line, go to the root folder of this repository,
then type ``python -m ridepooling`` into the terminal. A config path can be given as
an additional argument.

In PyCharm, this can be set up as a run configuration:

* create a new python configuration
* choose module name instead of script path
* input the module name ``ridepooling``
* set the root directory of this repository as the working directory

Example
-------



Features
--------

- etc

License
-------

The project is licensed under the MIT license.