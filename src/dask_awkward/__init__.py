from dask_awkward import config  # isort:skip; load awkward config


def __getattr__(value):
    import dask_awkward.lib

    return getattr(dask_awkward.lib, value)


original = dir()


def __dir__():
    import dask_awkward.lib

    return original + dir(dask_awkward.lib)
