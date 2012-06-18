#!/usr/bin/env python

from __future__ import print_function


"""
APHLA Module
-----------

This is an object-orient high level accelerator control library.

A procedural interface is provided.

   
:author: Lingyun Yang
:license:

Modules include:

    :mod:`aphla.machines`

        define machine specific settings, create lattice from channel
        finder service for different accelerator complex.

    :mod:`aphla.lattice`

        define the :class:`~aphla.lattice.CaElement`, :class:`~aphla.lattice.Twiss`,
        :class:`~aphla.lattice.Lattice` class

    :mod:`aphla.orbit`

        defines orbit retrieve routines

    :mod:`aphla.hlalib`

        defines procedural interface
        
"""

__version__ = "0.3.0b3"


import os
import tempfile
import logging

# for compatibilities with Python < 2.7
class NullHandler(logging.Handler):
    def emit(self, record):
        pass

#APHLA_LOG = os.path.join(tempfile.gettempdir(), "aphla.log")
APHLA_LOG = 'aphla.log'
logging.basicConfig(filename=APHLA_LOG,
    format='%(asctime)s - %(name)s [%(levelname)s]: %(message)s',
    level=logging.DEBUG)
# set null handler when logging for a library.
_h = NullHandler()
logging.getLogger('aphla').addHandler(_h)

#
from catools import *
from machines import initNSLS2VSR, initNSLS2VSRTwiss

#from rf import *
from hlalib import *
from ormdata import OrmData

from meastwiss import *
from aptools import *

import bba


# Added by Y. Hidaka
import curve_fitting
import current

