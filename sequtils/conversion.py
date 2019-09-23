# -*- coding: utf-8 -*-


# imports
# -------
import sys
if sys.version_info >= (3, 0):
    maketrans = str.maketrans
else:
    from string import maketrans


# constants
# ---------
COMPLEMENT_TABLE = None
CODON_TABLE = None
QSCORE_MAP = None


# functions
# ---------
def revcomplement(seq):
    """
    Reverse complement sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.revcomplement('AACCTT')
        'AAGGTT'
    """
    return complement(seq)[::-1]


def complement(seq):
    """
    Complement sequence.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.complement('AACCTT')
        TTGGAA
    """
    global COMPLEMENT_TABLE
    if COMPLEMENT_TABLE is None:
        COMPLEMENT_TABLE = maketrans('ATUGCYRSWKMBDHVNatugcyrswkmbdhvn', 'TAACGRYSWMKVHDBNtaacgryswmkvhdbn')
    return str(seq).translate(COMPLEMENT_TABLE)


def aa(seq):
    """
    Return amino acid translation of sequence. Ends of the sequences
    that don't produce a full codon will be clipped.

    Args:
        seq (str): Nucleotide sequence

    Examples:
        >>> sequtils.aa('ATGTAG')
        M*
    """
    global CODON_TABLE
    if CODON_TABLE is None:
        # TODO: figure out the right place for the pre-computed information here
        bases = ['T', 'C', 'A', 'G']
        codons = [a+b+c for a in bases for b in bases for c in bases]
        codons = codons + list(map(lambda x: x.lower(), codons))
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        amino_acids = amino_acids + amino_acids.lower()
        CODON_TABLE = dict(zip(codons, amino_acids))
    res = ''
    for i in range(0, len(seq) - 2, 3):
        res += CODON_TABLE[seq[i:(i+3)]]
    return res


def wrap(seq, bases=60):
    """
    Print wrapped sequence.

    Args:
        seq (str): Nucleotide sequence
        bases (int): Number of bases to include on each line.
    """
    count = 0
    ret = ''
    for i in seq:
        if count >= bases:
            ret = ret + '\n'
            count = 0
        ret = ret + i
        count += 1
    return ret


def likelihood(seq):
    """
    Translates quality scores sequence into error likelihoods.

    Args:
        seq (str): Sequence of quality scores.
    """
    global QSCORE_MAP
    if QSCORE_MAP is None:
        QSCORE_MAP = {'!': 1.0, '"': 0.7943282347242815, '#': 0.6309573444801932, '$': 0.5011872336272722, '%': 0.3981071705534972, '&': 0.31622776601683794, "'": 0.251188643150958, '(': 0.19952623149688797, ')': 0.15848931924611134, '*': 0.12589254117941673, '+': 0.1, ',': 0.07943282347242814, '-': 0.06309573444801933, '.': 0.05011872336272722, '/': 0.039810717055349734, '0': 0.03162277660168379, '1': 0.025118864315095794, '2': 0.0199526231496888, '3': 0.015848931924611134, '4': 0.012589254117941675, '5': 0.01, '6': 0.007943282347242814, '7': 0.00630957344480193, '8': 0.005011872336272725, '9': 0.003981071705534973, ':': 0.0031622776601683794, ';': 0.0025118864315095794, '<': 0.001995262314968879, '=': 0.001584893192461114, '>': 0.0012589254117941675, '?': 0.001, '@': 0.0007943282347242813, 'A': 0.000630957344480193, 'B': 0.0005011872336272725, 'C': 0.00039810717055349735, 'D': 0.00031622776601683794, 'E': 0.00025118864315095795, 'F': 0.00019952623149688788, 'G': 0.00015848931924611142, 'H': 0.00012589254117941674, 'I': 0.0001, 'J': 7.943282347242822e-05, 'K': 6.309573444801929e-05, 'L': 5.011872336272725e-05, 'M': 3.9810717055349695e-05, 'N': 3.1622776601683795e-05, 'O': 2.5118864315095822e-05, 'P': 1.9952623149688786e-05, 'Q': 1.584893192461114e-05, 'R': 1.2589254117941661e-05, 'S': 1e-05, 'T': 7.943282347242822e-06, 'U': 6.30957344480193e-06, 'V': 5.011872336272725e-06, 'W': 3.981071705534969e-06, 'X': 3.162277660168379e-06, 'Y': 2.5118864315095823e-06, 'Z': 1.9952623149688787e-06, '[': 1.584893192461114e-06, '\\': 1.2589254117941661e-06, ']': 1e-06, '^': 7.943282347242822e-07, '_': 6.30957344480193e-07, '`': 5.011872336272725e-07, 'a': 3.981071705534969e-07, 'b': 3.162277660168379e-07, 'c': 2.5118864315095823e-07, 'd': 1.9952623149688787e-07, 'e': 1.584893192461114e-07, 'f': 1.2589254117941662e-07, 'g': 1e-07, 'h': 7.943282347242822e-08, 'i': 6.30957344480193e-08, 'j': 5.011872336272725e-08, 'k': 3.981071705534969e-08, 'l': 3.162277660168379e-08, 'm': 2.511886431509582e-08, 'n': 1.9952623149688786e-08, 'o': 1.5848931924611143e-08, 'p': 1.2589254117941661e-08, 'q': 1e-08, 'r': 7.943282347242822e-09, 's': 6.309573444801943e-09, 't': 5.011872336272715e-09, 'u': 3.981071705534969e-09, 'v': 3.1622776601683795e-09, 'w': 2.511886431509582e-09, 'x': 1.9952623149688828e-09, 'y': 1.584893192461111e-09, 'z': 1.2589254117941663e-09, '{': 1e-09, '|': 7.943282347242822e-10, '}': 6.309573444801942e-10, '~': 5.011872336272714e-10, '\x7f': 3.9810717055349694e-10, '\x80': 3.1622776601683795e-10, '\x81': 2.511886431509582e-10, '\x82': 1.9952623149688828e-10, '\x83': 1.584893192461111e-10, '\x84': 1.2589254117941662e-10, '\x85': 1e-10}  ## noqa
    return [QSCORE_MAP[i] for i in seq]


def qscore(seq):
    """
    Translates quality score sequence into phred-scaled likelihoods.

    Args:
        seq (str): Sequence of quality scores.
    """
    return [ord(i)-33 for i in seq]
