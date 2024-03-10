"""
    swap_puzzle package initializer
"""

import os
from collections.abc import Callable
from abc import ABC, abstractmethod

from swap_puzzle.exception import *
from grid import Grid

from solver import Solver
from swap_puzzle.solvers import *
