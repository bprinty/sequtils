==========
Quickstart
==========

Overview
========

The `sequtils <http://atgtag.github.io/sequtils/latest>`_ module contains functions for calculating sequence-related distance and complexity metrics, commonly used in language processing and next-generation sequencing. It has a simple and consistent API that be used for investigating sequence characteristics:

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


It also has a :class:`sequtils.Sequence` object for object-based access to these properties:

.. code-block:: python

    >>> import sequtils
    >>> seq = sequtils.Sequence('AAAACCGT')
    >>> seq.hamming('AAAAGCGT')
    1
    >>> seq.gc_percent
    0.375
    >>> seq.revcomplement
    ACGTACGT
    >>> seq.dna_weight
    3895.59
    >>> # ... and so on ...


All of the metrics available in the repository are listed below, and can also be found in the `API <./api.html>`_ section of the documentation.


List of Available Functions
===========================

Sequence Quantification
-----------------------

+---------------------------------+------------------------------------------------------------+ 
| Function                        | Metric                                                     | 
+=================================+============================================================+ 
| :func:`sequtils.polydict`       | Length of longest homopolymer for all bases in sequence.   |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.polylength`     | Length of longest homopolymer in sequence.                 |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.entropy`        | Shannon entropy for bases in sequence.                     |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.gc_percent`     | Percentage of GC bases in sequence relative to all bases.  |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.gc_skew`        | GC skew for sequence:  (#G - #C)/(#G + #C).                |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.gc_shift`       | GC shift for sequence: (#A + #T)/(#G + #C)                 |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.dna_weight`     | Molecular weight for sequence with DNA backbone.           |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.rna_weight`     | Molecular weight for sequence with RNA backbone.           |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.aa_weight`      | Molecular weight for amino acid sequence.                  |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.zipsize`        | Compressibility of sequence.                               |
+---------------------------------+------------------------------------------------------------+


Domain Conversion
-----------------

+---------------------------------+------------------------------------------------------------+ 
| Function                        | Conversion                                                 | 
+=================================+============================================================+ 
| :func:`sequtils.revcomplement`  | Length of longest homopolymer for all bases in sequence.   |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.complement`     | Length of longest homopolymer in sequence.                 |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.aa`             | Shannon entropy for bases in sequence.                     |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.wrap`           | Percentage of GC bases in sequence relative to all bases.  |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.likelihood`     | GC skew for sequence:  (#G - #C)/(#G + #C).                |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.qscore`         | GC shift for sequence: (#A + #T)/(#G + #C)                 |
+---------------------------------+------------------------------------------------------------+


Distance Metrics
----------------

+---------------------------------+------------------------------------------------------------+ 
| Function                        | Distance Metric                                            | 
+=================================+============================================================+ 
| :func:`sequtils.hamming`        | Hamming distance between sequences.                        |
+---------------------------------+------------------------------------------------------------+
| :func:`sequtils.edit`           | Edit (levenshtein) distance between sequences              |
+---------------------------------+------------------------------------------------------------+


Utilities
---------

+------------------------------------+------------------------------------------------------------+ 
| Function                           | Utility                                                    | 
+====================================+============================================================+ 
| :func:`sequtils.random_sequence`   | Generate random sequence.                                  |
+------------------------------------+------------------------------------------------------------+
| :func:`sequtils.wrap`              | Newline-wrap sequence                                      |
+------------------------------------+------------------------------------------------------------+




