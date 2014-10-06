#!/usr/bin/env python
# -*- encoding: utf-8 -*-
""" Task1 of week 5"""

def bool_to_str(bvalue, short=False):

    """Gives the string value of True or False

    Arguments:
        bvalue (boolean): value to be converted
        short (boolean, optional): determines whether to return a
            short value.  Default value is False.

    Returns:
       string: Yes/Y or No/N which is the converted boolean value

    Examples:
        >>> bool_to_str(True)
        'Yes'

        >>> bool_to_str(False)
        'No'

        >>> bool_to_str(bvalue=True, short=True)
        'Y'
    """

    if bvalue:
        value = 'Yes'
    else:
        value = 'No'

    if short:
        value = value[0]

    return value
