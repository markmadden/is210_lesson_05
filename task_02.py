#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal
from decimal import Decimal

def get_interest_rate(principal, duration, prequalification=True):
    """Finds the interest rate.

        Args:
            principal (num): the value of the principal
            duration (num): the duration of the loan
            rate (num): the duration of the loan

        Returns:
            A decimal form of the interest rate or None if none exists.

        Examples:
            >>> get_interest_rate(15000,12,True)
            Decimal('0.0363')

            >>> get_interest_rate(1000000,20,False)
            None
            
    """

    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = Decimal('0.0363')
            else:
                rate = Decimal('0.0465')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = Decimal('0.0404')
            else:
                rate = Decimal('0.0498')
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = Decimal('0.0577')
            else:
                rate = Decimal('0.0639')
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = Decimal('0.0302')
            else:
                rate = Decimal('0.0398')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = Decimal('0.0327')
            else:
                rate = Decimal('0.0408')
        elif duration >= 21 and duration <= 30:
            if prequalification:
                rate = Decimal('0.0466')
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                rate = Decimal('0.0205')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                rate = Decimal('0.0262')
    else:
        rate = None
        
    return rate



def compound_interest(principal, duration, prequalification, interval=12):
    """Calculates the compound interest.

        Args:
            principal (num): the value of the principal
            duration (num): the duration of the loan
            rate (num): the duration of the loan
            interval (num): the number of times that interest is compounded
                    annually; defaults to 12

        Returns:
            The compounded interest and principal(combined) as a numeric type.

        Examples:
            >>> get_interest_rate(15000,12,True)
            Decimal('0.0363')

            >>> get_interest_rate(1000000,20,False)
            None
            
    """

    rate = Decimal(get_interest_rate(principal, duration, prequalification))
    total = Decimal(principal * ((1 + rate / interval) ** (interval * duration)))
    return Decimal(total)

def calculate_total(principal, duration, prequalification):
    """Returns the total amount owed over the life of the loan.

        Args:
            principal (num): the value of the principal
            duration (num): the duration of the loan
            rate (num): the duration of the loan

        Returns:
            The total amount, rounded to the nearest integer.  In the event that
            there is no interest rate for the passed argument, returns None.

        Examples:
            >>> get_interest_rate(15000,12,True)
            Decimal('0.0363')

            >>> get_interest_rate(1000000,20,False)
            None
            
    """
    
    rate = Decimal(get_interest_rate(principal, duration, prequalification))
    total = Decimal(compound_interest(
        principal, duration, prequalification, interval=12))
    return int(total)


def calculate_interest(principal, duration, prequalification):
    """Returns just the interest owed over the life of the loan.

        Args:
            principal (num): the value of the principal
            duration (num): the duration of the loan
            rate (num): the duration of the loan

        Returns:
            Only the interest owed over the life of the loan as an integer.

        Examples:
            >>> get_interest_rate(15000,12,True)
            Decimal('0.0363')

            >>> get_interest_rate(1000000,20,False)
            None
            
    """

    rate = Decimal(get_interest_rate(principal, duration, prequalification))
    total = Decimal(compound_interest(
        principal, duration, prequalification, interval=12))
    interest = Decimal(calculate_total(
        principal, duration, prequalification) - principal)
    return int(interest)
