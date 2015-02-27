# -*- coding: utf-8 -*-
"""
LAVEnder
~~~~~~~~

The LAVEnder Next-Generation Sequencing mappers evaluation tool.

:copyright: Copyright 2015 by Karel Brinda.
:license: MIT, see LICENSE for details.

.. module:: lavender
	:platform: Unix
	:synopsis: The LAVEnder Next-Generation Sequencing mappers evaluation tool.

.. moduleauthor:: Karel Brinda <karel.brinda@gmail.com>

"""

import os

__docformat__ = 'reStructuredText'
__all__=["Bam","Report","Panel"]

# todo:
#  - left-right: cigar correction
#  - threshold as a parameter

def include():
	return os.path.join( os.path.dirname(__file__), "lavender.snake")


__INPUT__ = []

def input():
	return __INPUT__

def add_input(input):
	__INPUT__.add(input)


__PANELS__ = []

def pannels():
	return __PANELS__

def add_panel(panel):
	__PANELS__.append(panel)

__BAMS__ = []

def bams():
	return __BAMS__

def add_bam(bam):
	__BAMS__.append(bam)


__REPORTS__ = []

def reports():
	return __REPORTS__

def add_report(report):
	__REPORTS__.append(report)


from .report import *
from .panel import *
from .bam import *

