"""
    swap_puzzle package initializer
"""

import os
from collections.abc import Callable
from collections import deque
from abc import ABC, abstractmethod

# type-hinting typedefs
cell = tuple[int, int]
state = list[list[int]]

from swap_puzzle.exception import *
from grid import Grid
from sp_utils import SPUtils

from solver import Solver
from swap_puzzle.solvers import *

from graph import Graph
