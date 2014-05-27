==================
CIS Sample Project
==================

:Author: Mark Biggers <biggers@utsl.com>
:Description: a Python code quiz
:Ref: _`restview, Restructured Text Viewer`: <https://pypi.python.org/pypi/restview>
:Revision: 1.1
:To View: restview README.rst
:Metainfo: `Introductory ReST docs <http://docutils.sf.net/rst.html>`_
:Date: 27 May 2014 (updated))

:Copyright: UTSL.com, 2013

-------------------------------------

.. contents:: **Table of Contents**

.. section-numbering::

-------------------------------------

Overview
========
We are following the email of 7/3/2013 on subject: **Python Project for CIS**.

Project Set-up
==============
-----------
Run GNUmake
-----------
Get the Makefile from the ``pml-tags-example`` Git project, to bootstrap. ::

 $ wget https://raw.github.com/biggers/pml-tags-example/master/Makefile

Get the project code from Github. ::

 $ make git_clone

Make "everything", to set up the project. ::

 $ make all

Run the Project
===============
--------------------
Running this project
--------------------
Activate the Python "virtual environment", and then run the project
with sample PML files. ::

 cd pml-tags-example

 . bin/activate

 ./cis_pml.py cis.pml

 ./cis_pml.py cis-1.pml

 ./cis_pml.py cis-2.pml

POSTLUDE: requirements
======================
*These project requirements are taken from the email noted above*.

A *PML document* is a standard HTML document with one additional feature. Any text between the starting ``<pml>`` tag and the ending ``</pml>`` tag, is interpreted as Python source code.

- There can be multiple PML blocks in a PML file.

- PML blocks will never nest.

- The standard HTML should pass through the parser untouched.

- The code within the PML tags should be executed with the python interpreter.

- A technique should be implemented to write data to the output stream from within the PML. In other words the python code should be able to define the output that will replace the PML.

- Variables and functions declared in one PML block should be available in subsequent PML blocks.

- PML should be able to handle indentation dependent upon the first non-whitespace line of python code. 

See the various ``*.pml`` (input) files, for examples.
