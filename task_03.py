#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts temperatures from one unit of measure to another."""


def celsius_to_farenheit(temperature):
    """Converts degrees celsius to degrees farenheit.

        Args:
            temperature (num): temperature in degrees celsius

        Returns:
            a numeric type of the temperature in degrees farenheit.

        Examples:
            >>> celsius_to_farenheit(42)
            107.6
    """

    f = float((9 * temperature)/5 + 32)
    return f

def farenheit_to_celsius(temperature):
    """Converts degrees farenheit to degrees celsius.

        Args:
            temperature (num): temperature in degrees farenheit

        Returns:
            a numeric type of the temperature in degrees celsius.

        Examples:
            >>> farenheit_to_celsius(42)
            5.0
    """

    c = float((5 * (temperature - 32))/9)
    return c

def convert_temperature(temperature, output_format='c'):
    """Detects type of temperature and outputs it as specified output type.

        Args:
            temperature (str): In the format of 35C or 45F with the
            Celsius or Farenheit symbol
            output_format (str): Accepts "c" or "f" as valid input;
            defaults to 'c'

        Returns:
            a numeric type of the temperature in the selected format.

        Examples:
            >>> convert_temperature('32F', 'c')
            0.0
            
    """
    temperature = temperature[0:-1]
    temperature = float(temperature)
    if output_format is 'c':
        result = farenheit_to_celsius(temperature)
    elif output_format is 'f':
        result = celsius_to_farenheit(temperature)
    else:
        result = None

    return float(result)
