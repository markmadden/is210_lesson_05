#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal


def get_interest_rate(principal, duration, prequalification):
    """Returns interest rate as a decimal.

    Args:
        principal(int): A numeric type, the value of the principal.
        duration(int): A numeric type, the duration of the loan
        prequalification(bool): A boolean, whether or not the loan is pre-
            qualified.

    Returns:
        A decimal form of the interest rate or None if none exists.

    Examples:

        >>>get_interest_rate(100000, 15, True)
        Decimal('0.0363')

        >>>get_interest_rate(1000000, 30, True)
        None

    """
    rate = None
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0363'
            else:
                rate = '0.0465'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0404'
            else:
                rate = '0.0498'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0577'
            else:
                rate = '0.0639'
        else:
            rate = None
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0302'
            else:
                rate = '0.0398'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0327'
            else:
                rate = '0.0408'
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = '0.0466'
        else:
            rate = None
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = '0.0205'
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = '0.0262'
        else:
            rate = None
    else:
        rate = None
    if rate is not None:
        rate = decimal.Decimal(rate)
    else:
        rate = None

    return rate


def compound_interest(principal, duration, rate, interval=12):
    """Calculates compound interest.

    Args:
        principal(int): A numeric type, the value of the principal.
        duration(int): A numeric type, the duration of the loan
        rate(decimal): A numeric type, the interest rate.
        interval(int, optional): A numeric type, defaults to 12, the number of
            times interest rate is compounded annually.

    Returns:
        A decimal form of the compound interest and principal(combined).

    Example:

        >>>compound_interest(100000, 15, decimal.Decimal('0.0363'))
        Decimal('172233.0130127978509806406311')

    """
    total = principal * ((1 + decimal.Decimal(rate) / interval) ** (interval
                                                                    * duration))
    return total


def calculate_total(principal, duration, prequalification):
    """Returns the total amount owed over the life of the loan.

    Args:
        principal(int): A numeric type, the value of the principal.
        duration(int): A numeric type, the duration of the loan
        prequalification(bool): A boolean, whether or not the loan is pre-
            qualified.

    Returns:
        Returns the total, rounded to the nearest integer. In the case of no
            interest rate the function returns None.

    Examples:

        >>>calculate_total(100000, 15, True)
        172233

        >>>calculate_total(1000000, 30, True)
        None
    """
    interest = get_interest_rate(principal, duration, prequalification)

    if interest is not None:
        total_two = compound_interest(principal, duration, interest)
        return int(round(total_two))
    else:
        return None


def calculate_interest(principal, duration, prequalification):
    """Returns just the interest owed over the life of the loan.

    Args:
        principal(int): A numeric type, the value of the principal.
        duration(int): A numeric type, the duration of the loan
        prequalification(bool): A boolean, whether or not the loan is pre-
            qualified.

    Returns:
        Returns the interest owed over the life of the loan, rounded to
            the nearest integer. In the case of no interest rate the function
            returns None.

    Examples:

        >>>calculate_interest(100000, 15, True)
        72233

        >>>calculate_interest(1000000, 20, False)
        None
    """
    total = calculate_total(principal, duration, prequalification)

    if total is not None:
        totaltwo = total - principal
        return totaltwo
    else:
        return None
