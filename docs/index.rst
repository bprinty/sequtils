======================================
Welcome to sequtils's documentation!
======================================


Overview
========

Python utilities for sequence comparison, quantification, and feature extraction.

The `sequtils <http://atgtag.github.io/sequtils/latest/index.html>`_ module contains functions for calculating sequence-related distance and complexity metrics, commonly used in language processing and next-generation sequencing:

.. code-block:: python

    >>> import sequtils
    >>> sequtils.hamming('ATTATT', 'ATTAGT')
    1
    >>> sequtils.edit('ATTATT', 'ATAGT')
    2
    >>> sequtils.polydict('AAAACCGT')
    {'A': 4, 'C': 2, 'G': 1, 'T': 1}
    >>> sequtils.polylength('AAAACCGT')
    4
    >>> sequtils.entropy('AGGATAAG')
    1.40
    >>> sequtils.gc_percent('AGGATAAG')
    0.375
    >>> sequtils.gc_skew('AGGATAAG')
    3.0
    >>> sequtils.gc_shift('AGGATAAG')
    1.67
    >>> sequtils.dna_weight('AGGATAAG')
    3968.59
    >>> sequtils.rna_weight('AGGATAAG')
    4082.59
    >>> sequtils.aa_weight('AGGATAAG')
    700.8
    >>> sequtils.zipsize('AGGATAAGAGATAGATTT')
    22


For more information on available functionality, see the `Quickstart <./quickstart.html>`_ section of the documentation.


Content
=======

.. toctree::
   :maxdepth: 3

   installation
   quickstart
   api


Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

