"""This module demonstrates basic Sphinx usage with Python modules.

Submodules
==========

.. autosummary::
    :toctree: _autosummary

    inner
"""

from .inner import add, Junk  # noqa

VERSION = "0.0.1"
"""The version of this module."""

