# -*- coding: utf-8 -*-


# imports
# -------
from gems import cached

from . import utils
from . import metrics
from . import distance
from . import conversion


# classes
# -------
class Sequence(object):
    """
    Object for managing sequence structure and operating
    on sequences (i.e. getting amino acid sequence, reverse
    complement, gc content, etc ...).

    Args:
        sequence (str): Nucleotide sequence.

    Examples:
        >>> seq = sequtils.Sequence('ACGTACGT')
        >>> seq.gc_content
        0.25
        >>> seq.revcomplement
        ACGTACGT
        >>> seq.dna_weight
        3895.59
    """

    def __init__(self, sequence):
        self.sequence = str(sequence)
        return

    def __str__(self):
        return self.sequence

    def __len__(self):
        return len(self.sequence)

    def __add__(self, other):
        if isinstance(other, Sequence):
            return Sequence(self.sequence + other.sequence)
        else:
            return Sequence(self.sequence + other)

    def __eq__(self, other):
        if isinstance(other, Sequence):
            return self.sequence == other.sequence
        else:
            return self.sequence == other

    def __contains__(self, other):
        if isinstance(other, Sequence):
            return other.sequence in self.sequence
        else:
            return other in self.sequence

    @cached
    def revcomplement(self):
        """
        Wrapper around :func:`sequtils.revcomplement`
        for the :class:`sequtils.Sequence` object.
        """
        return conversion.revcomplement(self.sequence)

    @cached
    def complement(self):
        """
        Wrapper around :func:`sequtils.complement`
        for the :class:`sequtils.Sequence` object.
        """
        return conversion.complement(self.sequence)

    @cached
    def aa(self):
        """
        Wrapper around :func:`sequtils.aa`
        for the :class:`sequtils.Sequence` object.
        """
        return conversion.aa(self.sequence)

    @cached
    def polydict(self):
        """
        Wrapper around :func:`sequtils.polydict`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.polydict(self.sequence)

    @cached
    def polylength(self):
        """
        Wrapper around :func:`sequtils.polylength`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.polylength(self.sequence)

    @cached
    def entropy(self):
        """
        Wrapper around :func:`sequtils.entropy`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.entropy(self.sequence)

    @cached
    def gc_percent(self):
        """
        Wrapper around :func:`sequtils.gc_percent`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.gc_percent(self.sequence)

    @cached
    def gc_skew(self):
        """
        Wrapper around :func:`sequtils.gc_skew`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.gc_skew(self.sequence)

    @cached
    def gc_shift(self):
        """
        Wrapper around :func:`sequtils.gc_shift`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.gc_shift(self.sequence)

    @cached
    def dna_weight(self):
        """
        Wrapper around :func:`sequtils.dna_weight`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.dna_weight(self.sequence)

    @cached
    def rna_weight(self):
        """
        Wrapper around :func:`sequtils.rna_weight`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.rna_weight(self.sequence)

    @cached
    def aa_weight(self):
        """
        Wrapper around :func:`sequtils.aa_weight`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.aa_weight(self.sequence)

    @cached
    def zipsize(self):
        """
        Wrapper around :func:`sequtils.zipsize`
        for the :class:`sequtils.Sequence` object.
        """
        return metrics.zipsize(self.sequence)

    def wrap(self, bases=60):
        """
        Wrapper around :func:`sequtils.wrap`
        for the :class:`sequtils.Sequence` object.

        Args:
            bases (int): Number of bases to include in line.
        """
        return utils.wrap(self.sequence, bases=bases)

    def hamming(self, other):
        """
        Wrapper around :func:`sequtils.hamming`
        for the :class:`sequtils.Sequence` object.

        Args:
            other (str, Sequence): Sequence to compare.
        """
        if isinstance(other, Sequence):
            return distance.hamming(self.sequence, other.sequence)
        else:
            return distance.hamming(self.sequence, other)

    def edit(self, other):
        """
        Wrapper around :func:`sequtils.edit`
        for the :class:`sequtils.Sequence` object.

        Args:
            other (str, Sequence): Sequence to compare.
        """
        if isinstance(other, Sequence):
            return distance.edit(self.sequence, other.sequence)
        else:
            return distance.edit(self.sequence, other)
