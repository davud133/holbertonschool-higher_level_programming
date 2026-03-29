#!/usr/bin/python3
"""Module that multiplies 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    try:
        return np.matmul(m_a, m_b)
    except Exception as e:
        msg = str(e)
        if ("did not contain a loop with signature matching types" in msg or
                "Scalar operands are not allowed" in msg):
            raise ValueError("Scalar operands are not allowed, use '*' instead")
        raise
