# -*- coding: utf-8 -*-

__author__ = 'bprinty'
__email__ = 'bprinty@gmail.com'
__version__ = '0.1.0'


# metrics
from .metrics import polydict         ## noqa
from .metrics import polylength       ## noqa
from .metrics import entropy          ## noqa
from .metrics import gc_percent       ## noqa
from .metrics import gc_skew          ## noqa
from .metrics import gc_shift         ## noqa
from .metrics import dna_weight       ## noqa
from .metrics import rna_weight       ## noqa
from .metrics import aa_weight        ## noqa
from .metrics import zipsize          ## noqa


# conversion
from .conversion import revcomplement ## noqa
from .conversion import complement    ## noqa
from .conversion import aa            ## noqa
from .conversion import wrap          ## noqa
from .conversion import likelihood    ## noqa
from .conversion import qscore        ## noqa


# distance
from .distance import hamming         ## noqa
from .distance import edit            ## noqa


# utils
from .utils import random_sequence    ## noqa
from .utils import wrap               ## noqa


# objects
from .objects import Sequence         ## noqa
