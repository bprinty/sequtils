# -*- coding: utf-8 -*-


import unittest
from nose.tools import nottest
from nose_parameterized import parameterized

import sequtils


class TestConversion(unittest.TestCase):

    @parameterized.expand((
        ('ACGT', 'ACGT'),
        ('AAAAAAAAAAA', 'TTTTTTTTTTT'),
        ('ATGACTGAATATAAACTTGT', 'ACAAGTTTATATTCAGTCAT'),
    ))
    def test_revcomplement(self, sequence, res):
        self.assertEqual(sequtils.revcomplement(sequence), res)
        return

    @parameterized.expand((
        ('ACGT', 'TGCA'),
        ('AAAAAAAAAAA', 'TTTTTTTTTTT'),
        ('ATGACTGAATATAAACTTGT', 'TACTGACTTATATTTGAACA'),
    ))
    def test_complement(self, sequence, res):
        self.assertEqual(sequtils.complement(sequence), res)
        return

    @parameterized.expand((
        ('ACGT', 'T'),
        ('GGGGGGGGGG', 'GGG'),
        ('ATGACTGAATATAAACTTGT', 'MTEYKL'),
    ))
    def test_aa(self, sequence, res):
        self.assertEqual(sequtils.aa(sequence), res)
        return

    @parameterized.expand((
        ('*', [0.12589254117941673]),
        ('I@+', [0.0001, 0.0007943282347242813, 0.1]),
    ))
    def test_likelihood(self, sequence, res):
        self.assertEqual(sequtils.likelihood(sequence), res)
        return

    @parameterized.expand((
        ('*', [9]),
        ('I@+', [40, 31, 10]),
    ))
    def test_qscore(self, sequence, res):
        self.assertEqual(sequtils.qscore(sequence), res)
        return
