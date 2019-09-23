# -*- coding: utf-8 -*-


import unittest
from parameterized import parameterized

import sequtils


class TestDistance(unittest.TestCase):

    @parameterized.expand((
        ('ACGT', 'ACGT', 0),
        ('AAAAAAAAAAA', 'AAAAAAATAAA', 1),
        ('ATGACTGAATATAAACTTGT', 'ATGACTCATTATGAACTTGT', 3),
    ))
    def test_hamming(self, sequence, other, res):
        self.assertEqual(sequtils.hamming(sequence, other), res)
        return

    @parameterized.expand((
        ('ACGT', 'ATGT', 1),
        ('AAAAAAAAAAA', 'AAAAAATAA', 3),
        ('ATGACTGAATATAAACTTGT', 'ATGACTGAATTAGTAAAAACTTGT', 4),
    ))
    def test_edit(self, sequence, other, res):
        self.assertEqual(sequtils.edit(sequence, other), res)
        return