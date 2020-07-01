"""Collection of numpy wrapper functions."""
from .absolute import absolute as abs, absolute
from .add import add
from .amax import amax, amax as max
from .amin import amin, amin as min
from .any import any
from .all import all
from .allclose import allclose
from .apply_along_axis import apply_along_axis
from .apply_over_axes import apply_over_axes
from .argmax import argmax
from .argmin import argmin
from .around import around, around as round, around as round_
from .array_repr import array_repr
from .array_split import array_split
from .array_str import array_str
from .atleast_1d import atleast_1d
from .atleast_2d import atleast_2d
from .atleast_3d import atleast_3d
from .broadcast_arrays import broadcast_arrays
from .ceil import ceil
from .choose import choose
from .common_type import common_type
from .concatenate import concatenate
from .count_nonzero import count_nonzero
from .cumsum import cumsum
from .diag import diag
from .diagonal import diagonal
from .true_divide import true_divide, true_divide as divide
from .divmod import divmod
from .dsplit import dsplit
from .dstack import dstack
from .equal import equal
from .expand_dims import expand_dims
from .floor import floor
from .floor_divide import floor_divide
from .greater import greater
from .greater_equal import greater_equal
from .hstack import hstack
from .hsplit import hsplit
from .less import less
from .less_equal import less_equal
from .inner import inner
from .isclose import isclose
from .isfinite import isfinite
from .logical_and import logical_and
from .logical_or import logical_or
from .matmul import matmul
from .maximum import maximum
from .minimum import minimum
from .mean import mean
from .moveaxis import moveaxis
from .multiply import multiply
from .negative import negative
from .nonzero import nonzero
from .not_equal import not_equal
from .ones import ones
from .outer import outer
from .positive import positive
from .power import power
from .prod import prod
from .remainder import remainder as mod, remainder
from .repeat import repeat
from .reshape import reshape
from .rint import rint
from .split import split
from .square import square
from .stack import stack
from .subtract import subtract
from .sum import sum
from .tile import tile
from .transpose import transpose
from .vsplit import vsplit
from .vstack import vstack
from .where import where
from .zeros import zeros
