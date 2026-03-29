#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy."""
    try:
        return np.dot(m_a, m_b)
    except Exception as e:
        msg = str(e)

        if (
            "ufunc 'multiply' did not contain a loop with "
            "signature matching types" in msg
        ):
            raise ValueError(
                "Scalar operands are not allowed, use '*' instead"
            )

        if "data type must provide an itemsize" in msg:
            raise TypeError("invalid data type for einsum")

        if "setting an array element with a sequence." in msg:
            raise ValueError("setting an array element with a sequence.")

        raise
