"""The inner module implements ``add`` and class ``Junk``
"""


def add(a, b):
    """Adds ``a`` to ``b``.

    Parameters
    ----------
    a : any
        First argument to add.
    b : type of a
        Second argument to add.

    Returns
    -------
    type of a:
        The result of ``a + b``.
    """
    return a + b


class Junk:
    """My Junk class"""

    def add(self, a, b):
        """Adds ``a`` to ``b``.

        Parameters
        ----------
        a : any
            First argument to add.
        b : type of a
            Second argument to add.

        Returns
        -------
        type of a:
            The result of ``a + b``.
        """
        return a + b
