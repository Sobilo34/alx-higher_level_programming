#!/usr/bin/python3
"""
This is a Locked Class Module
"""


class LockedClass:
    """
    This class enforces the instantiation of a single attribute, 'first_name.
    """
    __slots__ = ["first_name"]
