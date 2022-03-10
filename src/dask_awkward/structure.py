from __future__ import annotations

from typing import Any

import awkward._v2 as ak
import numpy as np

from .core import (
    DaskAwkwardNotImplemented,
    TrivialPartitionwiseOp,
    map_partitions,
    new_known_scalar,
    pw_reduction_with_agg_to_scalar,
)
from .utils import borrow_docstring

__all__ = (
    "argcartesian",
    "argcombinations",
    "argsort",
    "broadcast_arrays",
    "cartesian",
    "combinations",
    "concatenate",
    "copy",
    "fill_none",
    "firsts",
    "flatten",
    "from_regular",
    "full_like",
    "isclose",
    "is_none",
    "local_index",
    "mask",
    "nan_to_num",
    "num",
    "ones_like",
    "packed",
    "pad_none",
    "ravel",
    "run_lengths",
    "singletons",
    "sort",
    "strings_astype",
    "to_regular",
    "unflatten",
    "unzip",
    "values_astype",
    "where",
    "with_field",
    "with_name",
    "with_parameter",
    "without_parameters",
    "zeros_like",
    "zip",
)

_num_trivial = TrivialPartitionwiseOp(ak.num, axis=1)


@borrow_docstring(ak.argcartesian)
def argcartesian(
    arrays,
    axis=1,
    nested=None,
    parameters=None,
    with_name=None,
    highlevel=True,
    behavior=None,
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.argcombinations)
def argcombinations(
    array,
    n,
    replacement=False,
    axis=1,
    fields=None,
    parameters=None,
    with_name=None,
    highlevel=True,
    behavior=None,
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.argsort)
def argsort(array, axis=-1, ascending=True, stable=True, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.broadcast_arrays)
def broadcast_arrays(*arrays, **kwargs):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.cartesian)
def cartesian(
    arrays,
    axis=1,
    nested=None,
    parameters=None,
    with_name=None,
    highlevel=True,
    behavior=None,
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.combinations)
def combinations(
    array,
    n,
    replacement=False,
    axis=1,
    fields=None,
    parameters=None,
    with_name=None,
    highlevel=True,
    behavior=None,
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.concatenate)
def concatenate(
    arrays, axis=0, merge=True, mergebool=True, highlevel=True, behavior=None
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.copy)
def copy(array):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.fill_none)
def fill_none(array, value, axis=-1, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.firsts)
def firsts(array, axis=1, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.flatten)
def flatten(array, axis=1, highlevel=True, behavior=None):
    return map_partitions(
        ak.flatten,
        array,
        axis=axis,
        highlevel=highlevel,
        behavior=behavior,
    )


@borrow_docstring(ak.from_regular)
def from_regular(array, axis=1, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.full_like)
def full_like(array, fill_value, highlevel=True, behavior=None, dtype=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.isclose)
def isclose(
    a, b, rtol=1e-05, atol=1e-08, equal_nan=False, highlevel=True, behavior=None
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.is_none)
def is_none(array, axis=0, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.local_index)
def local_index(array, axis=-1, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.mask)
def mask(array, mask, valid_when=True, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.nan_to_num)
def nan_to_num(
    array, copy=True, nan=0.0, posinf=None, neginf=None, highlevel=True, behavior=None
):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.num)
def num(array: Any, axis: int | None = 1, highlevel: bool = True, behavior=None) -> Any:
    if axis == 1:
        return map_partitions(
            ak.num, array, axis=axis, highlevel=highlevel, behavior=behavior
        )
    if axis == 0:
        if array.known_divisions:
            return new_known_scalar(array.divisions[-1], dtype=int)
        else:
            return pw_reduction_with_agg_to_scalar(
                array,
                ak.num,
                axis=0,
                dtype=np.int64,
                agg=ak.sum,
                agg_kwargs={"axis": None},
                highlevel=highlevel,
                behavior=behavior,
            )
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.ones_like)
def ones_like(array, highlevel=True, behavior=None, dtype=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.packed)
def packed(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.pad_none)
def pad_none(array, target, axis=1, clip=False, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.ravel)
def ravel(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.run_lengths)
def run_lengths(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.singletons)
def singletons(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.sort)
def sort(array, axis=-1, ascending=True, stable=True, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.strings_astype)
def strings_astype(array, to, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.to_regular)
def to_regular(array, axis=1, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.unflatten)
def unflatten(array, counts, axis=0, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.unzip)
def unzip(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.values_astype)
def values_astype(array, to, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.where)
def where(condition, *args, **kwargs):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.with_field)
def with_field(base, what, where=None, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.with_name)
def with_name(array, name, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.with_parameter)
def with_parameter(array, parameter, value, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.without_parameters)
def without_parameters(array, highlevel=True, behavior=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.zeros_like)
def zeros_like(array, highlevel=True, behavior=None, dtype=None):
    raise DaskAwkwardNotImplemented("TODO")


@borrow_docstring(ak.zip)
def zip(
    arrays,
    depth_limit=None,
    parameters=None,
    with_name=None,
    highlevel=True,
    behavior=None,
    right_broadcast=False,
):
    raise DaskAwkwardNotImplemented("TODO")
