#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides loan management features."""

import decimal

def get_interest_rate(principal, duration, prequalification):

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

    total = principal * ((1 + decimal.Decimal(rate) / interval) ** (interval
                                                                    * duration))
    return total

def calculate_total(principal, duration, prequalification):

    interest = get_interest_rate(principal, duration, prequalification)

    if interest is not None:
        total_two = compound_interest(principal, duration, interest)
        return int(round(total_two))
    else:
        return None

def calculate_interest(principal, duration, prequalification):

    total = calculate_total(principal, duration, prequalification)

    if total is not None:
        totaltwo = total - principal
        return totaltwo
    else:
        return None
