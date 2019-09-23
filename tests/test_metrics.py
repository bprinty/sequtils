# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

import sequtils


class TestMetrics(unittest.TestCase):

    @parameterized.expand((
        ('ACGT', {'A': 1, 'C': 1, 'T': 1, 'G': 1}),
        ('AAAAAAAAAAA', {'A': 11, 'C': 0, 'T': 0, 'G': 0}),
        ('ATGACTGAATATAAACTTGT', {'A': 3, 'C': 1, 'T': 2, 'G': 1}),
    ))
    def test_polydict(self, sequence, res):
        self.assertEqual(sequtils.polydict(sequence), res)
        return

    @parameterized.expand((
        ('ACGT', 1),
        ('AAAAAAAAAAA', 11),
        ('ATGACTGAATATAAACTTGT', 3),
    ))
    def test_polylength(self, sequence, res):
        self.assertEqual(sequtils.polylength(sequence), res)
        return

    @parameterized.expand((
        ('ACGT', 2.0),
        ('AAAAAAAAAAA', 0),
        ('ATGACTGAATATAAACTTGT', 1.80),
    ))
    def test_entropy(self, sequence, res):
        self.assertEqual(round(sequtils.entropy(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 0.5),
        ('AAAAAAAAAAA', 0),
        ('ATGACTGAATATAAACTTGT', 0.25),
    ))
    def test_gc_percent(self, sequence, res):
        self.assertEqual(round(sequtils.gc_percent(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 0),
        ('AAAAAAAAAAA', 0.0),
        ('ATGACTGAATATAAACTTGT', 1.0),
    ))
    def test_gc_skew(self, sequence, res):
        self.assertEqual(round(sequtils.gc_skew(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 1.0),
        ('AAAAAAAAAAA', 11.0),
        ('ATGACTGAATATAAACTTGT', 3.0),
    ))
    def test_gc_shift(self, sequence, res):
        self.assertEqual(round(sequtils.gc_shift(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 1947.8),
        ('AAAAAAAAAAA', 5403.2),
        ('ATGACTGAATATAAACTTGT', 9761),
    ))
    def test_dna_weight(self, sequence, res):
        self.assertEqual(round(sequtils.dna_weight(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 1997.8),
        ('AAAAAAAAAAA', 5579.2),
        ('ATGACTGAATATAAACTTGT', 9983.0),
    ))
    def test_rna_weight(self, sequence, res):
        self.assertEqual(round(sequtils.rna_weight(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 404.5),
        ('AAAAAAAAAAA', 980.1),
        ('ATGACTGAATATAAACTTGT', 2014.2),
    ))
    def test_aa_weight(self, sequence, res):
        self.assertEqual(round(sequtils.aa_weight(sequence), 2), res)
        return

    @parameterized.expand((
        ('ACGT', 12),
        ('AAAAAAAAAAA', 11),
        ('ATGACTGAATATAAACTTGT', 23),
    ))
    def test_zipsize(self, sequence, res):
        self.assertEqual(sequtils.zipsize(sequence), res)
        return

