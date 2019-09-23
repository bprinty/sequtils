# -*- coding: utf-8 -*-


# imports
# -------
import sys
import editdistance as ed
if sys.version_info >= (3, 0):
    imap = map
else:
    from itertools import imap


# functions
# ---------
def hamming(seq1, seq2):
    """
    Calculate hamming distance between sequences.

    Args:
        seq1 (str): Reference sequence
        seq2 (str): Sequence to compare

    Examples:
        >>> hamming('AACCTT', 'AAGCCTT')
        1
    """
    return sum(imap(str.__ne__, str(seq1), str(seq2)))


def edit(seq1, seq2):
    """
    Wrapper around editdistance.eval for fast Levenshtein
    distance computation.

    Args:
        seq1 (str): Reference sequence
        seq2 (str): Sequence to compare

    Examples:
        >>> edit('banana', 'bahama')
        2
    """
    return int(ed.eval(seq1, seq2))
