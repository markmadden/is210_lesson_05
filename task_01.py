#!usr/bin/env python
# -*- codng: utf-8 -*-
"""Basic function practice."""


def bool_to_str(bvalue, short=False):
    """Converts a boolean to a string.

        Args:
            bvalue (bool): A boolean that is converted to a string.
            short (bool): If True, produces a short response of "Y" or "N"

        Returns:
            A string; Yes if bvalue is True, and No if bvalue is false.
            Short defaults to False.  If true, produces a response of "Y" if
            bvalue is True and "N" if bvalue is False.

        Examples:

    """

    if bvalue is True:
        result = "Yes"
        if short:
            result = "Y"
    elif bvalue is False:
        result = "No"
        if short:
            result = "N"
    else:
        result = "None"

    return result
