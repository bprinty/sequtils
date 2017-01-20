# -*- coding: utf-8 -*-


import unittest
from nose.tools import nottest
from nose_parameterized import parameterized

import sequtils


class TestUtils(unittest.TestCase):

    @parameterized.expand((
        (20, 'AC'),
        (5, 'ACGT'),
    ))
    def test_random_sequence(self, slen, tmpl):
        rs = sequtils.random_sequence(slen, tmpl)
        self.assertEqual(len(rs), slen)
        return

    @parameterized.expand((
        ('ACGT', 2, 'AC\nGT'),
        ('AAAAAAAAAAA', 3, 'AAA\nAAA\nAAA\nAA'),
    ))
    def test_wrap(self, sequence, bases, res):
        self.assertEqual(sequtils.wrap(sequence, bases=bases), res)
        return

