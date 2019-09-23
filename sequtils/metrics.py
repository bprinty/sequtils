# -*- coding: utf-8 -*-


# imports
# -------
from zlib import compress
import re
from math import log


# functions
# ---------
def polydict(seq, nuc='ACGT'):
    """
    Computes largest homopolymer for all specified
    nucleotides.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.polydict('AAAACCGT')
        {'A': 4, 'C': 2, 'G': 1, 'T': 1}
    """
    ret = {}
    for base in nuc:
        lens = []
        for i in re.findall(base + '+', seq):
            lens.append(len(i))
        ret[base] = max(lens) if lens else 0
    return ret


def polylength(seq):
    """
    Calculate length of maximum homopolymer stretch
    within sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.polylength('AAAACCGT')
        4
    """
    return max(polydict(seq).values())


def entropy(seq):
    """
    Calculate Shannon entropy of sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.entropy('AGGATAAG')
        1.40
        >>> sequtils.entropy('AAAACCGT')
        1.75
    """
    cnt = [seq.count(i) for i in 'ACGT']
    d = sum(cnt)
    ent = []
    for i in [float(i)/d for i in cnt]:
        # round corner case that would cause math domain error
        if i == 0:
            i = 1
        ent.append(i * log(i, 2))
    return -1 * sum(ent)


def gc_percent(seq):
    """
    Calculate fraction of GC bases within sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.gc_percent('AGGATAAG')
        0.375
    """
    counts = [seq.count(i) for i in 'ACGT']
    gc = float(counts[1] + counts[2])/sum(counts)
    return gc


def gc_skew(seq):
    """
    Calculate GC skew (g-c)/(g+c) for sequence. For
    homopolymer stretches with no GC, the skew will be rounded
    to zero.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.gc_skew('AGGATAAG')
        3.0
    """
    g = seq.count('G')
    c = seq.count('C')
    d = float(g + c)
    if d == 0:
        d = 1
    return float(g - c)/1


def gc_shift(seq):
    """
    Calculate GC shift (a + t)/(g + c) for sequence. For
    homopolymer stretches with no GC, the shift will be rounded to
    the number of bases in the sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.gc_shift('AGGATAAG')
        1.67
    """
    g = seq.count('G')
    c = seq.count('C')
    a = seq.count('A')
    t = seq.count('T') + seq.count('U')
    d = float(g + c)
    if d == 0:
        d = 1
    return float(a + t)/d


def dna_weight(seq):
    """
    Return molecular weight of triphosphate dna sequence (g/mol).

    See https://www.thermofisher.com/us/en/home/references/ambion-tech-support/rna-tools-and-calculators/dna-and-rna-molecular-weights-and-conversions.html
    for details on conversions.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.dna_weight('AGGATAAG')
        3968.59
    """
    wmap = {'A': 491.2, 'C': 467.2, 'G': 507.2, 'T': 482.2, 'N': 487.0}
    return sum([wmap[i] for i in seq])


def rna_weight(seq):
    """
    Return molecular weight of triphosphate rna sequence (g/mol).

    See https://www.thermofisher.com/us/en/home/references/ambion-tech-support/rna-tools-and-calculators/dna-and-rna-molecular-weights-and-conversions.html
    for details on conversions.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.rna_weight('AGGATAAG')
        4082.59
    """
    wmap = {'A': 507.2, 'C': 483.2, 'G': 523.2, 'T': 484.2, 'U': 484.2, 'N': 499.5}
    return sum([wmap[i] for i in seq])


def aa_weight(seq):
    """
    Return molecular weight of amino acid sequence (g/mol).

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.aa_weight('AGGATAAG')
        700.8
    """
    wmap = {'A': 89.1, 'R': 174.2, 'N': 132.1, 'D': 133.1, 'C': 121.2, 'E': 147.1, 'Q': 146.2, 'G': 75.1, 'H': 155.2, 'I': 131.2, 'L': 131.2, 'K': 146.2, 'M': 149.2, 'F': 165.2, 'P': 115.1, 'S': 105.1, 'T': 119.1, 'W': 204.2, 'Y': 181.2, 'V': 117.1}  ## noqa
    return sum([wmap[i] for i in seq.replace('*', '')])


def zipsize(seq):
    """
    Calculate size of gzip-compressed sequence.

    Args:
        seq (str): Sequence

    Examples:
        >>> sequtils.zipsize('AGGATAAGAGATAGATTT')
        39.31
    """
    return len(compress(seq.encode()))
