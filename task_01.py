#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Code."""


def bool_to_str(bvalue, short=False):
    """Converts a boolean to a string (short or long).

    Args:
        bvalue(bool): A boolen that is converted to a string.
        short(bool), optional): If False, bvalue will return as a whole
            word ('Yes' or 'No') else a single letter ('Y', 'N').

    Returns:
        string: 'Yes' if bvalue is True or 'No' if bvalue is False.

    Examples:

        >>>bool_to_str(True)
        'Yes'

        >>>bool_to_str(False)
        'No'

        >>>bool_to_str(False, short = True)
        'N'
    """
    if bvalue is True:
        return 'Yes' if short is False else 'Y'
    elif bvalue is False:
        return 'No' if short is False else 'N'
