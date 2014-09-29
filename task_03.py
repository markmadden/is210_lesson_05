#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 Code."""


def celsius_to_fahrenheit(temperature):
    """Converts temperatures from celsius to fahrenheit.

    Args:
        temperature(num): A numeric type that reads in a temperature in celsius. 

    Returns:
        float: Converts the temperature and output is in fahrenheit.

    Example:

        >>>celsius_to_fahrenheit(42)
        107.6

    """
    fahren = float(9.0 * temperature / 5.0 + 32.0)

    return fahren


def fahrenheit_to_celsius(temperature):
    """Converts temperatures from fahrenheit to celsius.

    Args:
        temperature(num): A numeric type that reads in a temperature in
            fahrenheit.

    Returns:
        float: Converts the temperature and output is in celsius.

    Example:

        >>>fahrenheit_to_celsius(42)
        5.555555555555555

    """
    celsi = float(5.0 * (temperature - 32.0) / 9.0)

    return celsi


def convert_temperature(temperature, output_format='c'):
    """Converts temperatures from fahrenheit to celsiu or vice versa. 

    Args:
        temperature(num): A numeric type that reads in a temperature in
            fahrenheit or celsius.
        output_format(str, optional): A stirng that determines the output of
            the temperature. Default is celsius.

    Returns:
        float: Converts the temperature and output is in celsius or fahrenheit.
            Returns None if conditions are not met. 

    Example:

        >>>convert_temperature('42F','c')
        5.555555555555555

        >>>convert_temperature('42C','f')
        107.6

        >>>convert_temperature('42C','c')
        42.0

        >>>convert_temperature('42C','p')
        None

    """
    incoming = str(temperature[-1:])
    temperature = float(temperature[:-1])

    if incoming == 'F':
        if output_format == 'c':
            outputtemp = fahrenheit_to_celsius(temperature)
        elif output_format == 'f':
            outputtemp = temperature
        else:
            outputtemp = None
    elif incoming == 'C':
        if output_format == 'f':
            outputtemp = celsius_to_fahrenheit(temperature)
        elif output_format == 'c':
            outputtemp = temperature     
        else:
            outputtemp = None
    else:
        outputtemp = None

    return outputtemp
