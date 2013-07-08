==================
CIS Sample Project
==================

:Author: Mark Biggers <biggers@utsl.com>
:Description: a Python code quiz
:Ref: _`restview, Restructured Text Viewer`: <https://pypi.python.org/pypi/restview>
:Revision: 1.0
:To View: restview README.rst
:Metainfo: `Introductory ReST docs <http://docutils.sf.net/rst.html>`_
:Date: 8 July 2013

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
