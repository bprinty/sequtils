# -*- coding: utf-8 -*-


import unittest
from nose.tools import nottest
from nose_parameterized import parameterized

import sequtils


class TestSequence(unittest.TestCase):

    def test_properties(self):
        s = sequtils.Sequence('ACGT')
        self.assertEqual(s.sequence, 'ACGT')
        return

    def test_operators(self):
        s1 = sequtils.Sequence('ACGT')
        # add
        res = s1 + 'AAAA'
        self.assertEqual(res.sequence, 'ACGTAAAA')
        res = s1 + sequtils.Sequence('AAAA')
        self.assertEqual(res, 'ACGTAAAA')
        # contains
        self.assertTrue('CG' in res)
        self.assertTrue('AAA' in res)
        self.assertFalse('AGAGAGAG' in res)
        # len
        self.assertEqual(len(res), 8)
        return

    @parameterized.expand((
        ('ACGT', 'ACGT'),
        ('AAAAAAAAAAA', 'TTTTTTTTTTT'),
        ('ATGACTGAATATAAACTTGT', 'ACAAGTTTATATTCAGTCAT'),
    ))
    def test_revcomplement(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.revcomplement, res)
        return

    @parameterized.expand((
        ('ACGT', 'TGCA'),
        ('AAAAAAAAAAA', 'TTTTTTTTTTT'),
        ('ATGACTGAATATAAACTTGT', 'TACTGACTTATATTTGAACA'),
    ))
    def test_complement(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.complement, res)
        return

    @parameterized.expand((
        ('ACGT', 'T'),
        ('GGGGGGGGGG', 'GGG'),
        ('ATGACTGAATATAAACTTGT', 'MTEYKL'),
    ))
    def test_aa(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.aa, res)
        return

    @parameterized.expand((
        ('ACGT', {'A': 1, 'C': 1, 'T': 1, 'G': 1}),
        ('AAAAAAAAAAA', {'A': 11, 'C': 0, 'T': 0, 'G': 0}),
        ('ATGACTGAATATAAACTTGT', {'A': 3, 'C': 1, 'T': 2, 'G': 1}),
    ))
    def test_polydict(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.polydict, res)
        return

    @parameterized.expand((
        ('ACGT', 1),
        ('AAAAAAAAAAA', 11),
        ('ATGACTGAATATAAACTTGT', 3),
    ))
    def test_polylength(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.polylength, res)
        return

    @parameterized.expand((
        ('ACGT', 2.0),
        ('AAAAAAAAAAA', 0),
        ('ATGACTGAATATAAACTTGT', 1.80),
    ))
    def test_entropy(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(round(obj.entropy, 2), res)
        return

    @parameterized.expand((
        ('ACGT', 0.5),
        ('AAAAAAAAAAA', 0),
        ('ATGACTGAATATAAACTTGT', 0.25),
    ))
    def test_gc_percent(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.gc_percent, res)
        return

    @parameterized.expand((
        ('ACGT', 0),
        ('AAAAAAAAAAA', 0.0),
        ('ATGACTGAATATAAACTTGT', 1.0),
    ))
    def test_gc_skew(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.gc_skew, res)
        return

    @parameterized.expand((
        ('ACGT', 1.0),
        ('AAAAAAAAAAA', 11.0),
        ('ATGACTGAATATAAACTTGT', 3.0),
    ))
    def test_gc_shift(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.gc_shift, res)
        return

    @parameterized.expand((
        ('ACGT', 1947.8),
        ('AAAAAAAAAAA', 5403.2),
        ('ATGACTGAATATAAACTTGT', 9761),
    ))
    def test_dna_weight(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(round(obj.dna_weight, 2), res)
        return

    @parameterized.expand((
        ('ACGT', 1997.8),
        ('AAAAAAAAAAA', 5579.2),
        ('ATGACTGAATATAAACTTGT', 9983.0),
    ))
    def test_rna_weight(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(round(obj.rna_weight, 2), res)
        return

    @parameterized.expand((
        ('ACGT', 404.5),
        ('AAAAAAAAAAA', 980.1),
        ('ATGACTGAATATAAACTTGT', 2014.2),
    ))
    def test_aa_weight(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(round(obj.aa_weight, 2), res)
        return

    @parameterized.expand((
        ('ACGT', 12),
        ('AAAAAAAAAAA', 11),
        ('ATGACTGAATATAAACTTGT', 23),
    ))
    def test_zipsize(self, sequence, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.zipsize, res)
        return

    @parameterized.expand((
        ('ACGT', 2, 'AC\nGT'),
        ('AAAAAAAAAAA', 3, 'AAA\nAAA\nAAA\nAA'),
    ))
    def test_wrap(self, sequence, bases, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.wrap(bases=bases), res)
        return

    @parameterized.expand((
        ('ACGT', 'ACGT', 0),
        ('AAAAAAAAAAA', 'AAAAAAATAAA', 1),
        ('ATGACTGAATATAAACTTGT', 'ATGACTCATTATGAACTTGT', 3),
    ))
    def test_hamming(self, sequence, other, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.hamming(other), res)
        return

    @parameterized.expand((
        ('ACGT', 'ATGT', 1),
        ('AAAAAAAAAAA', 'AAAAAATAA', 3),
        ('ATGACTGAATATAAACTTGT', 'ATGACTGAATTAGTAAAAACTTGT', 4),
    ))
    def test_edit(self, sequence, other, res):
        obj = sequtils.Sequence(sequence)
        self.assertEqual(obj.edit(other), res)
        return
