#!/usr/bin/python3
"""defines MyInt class inherited from int class"""


class MyInt(int):
    """defines MyInt class"""
    def __eq__(self, other):
        """checks if not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """checks if equal"""
        return super().__eq__(other)
