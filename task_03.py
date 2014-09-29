#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Converts temperatures from one unit of measure to another."""


def celsius_to_fahrenheit(temperature):
    """Converts degrees celsius to degrees fahrenheit.

        Args:
            temperature (num): temperature in degrees celsius

        Returns:
            a numeric type of the temperature in degrees fahrenheit.

        Examples:
            >>> celsius_to_fahrenheit(42)
            107.6
    """

    fahrenheit = (9 * temperature)/5 + 32.0
    return fahrenheit


def fahrenheit_to_celsius(temperature):
    """Converts degrees fahrenheit to degrees celsius.

        Args:
            temperature (num): temperature in degrees fahrenheit

        Returns:
            a numeric type of the temperature in degrees celsius.

        Examples:
            >>> fahrenheit_to_celsius(42)
            5.0
    """

    celsius = (5 * (temperature - 32))/9.0
    return celsius


def convert_temperature(temperature, output_format='c'):
    """Detects type of temperature and outputs it as specified output type.

        Args:
            temperature (str): In the format of 35C or 45F with the
            Celsius or Fahrenheit symbol
            output_format (str): Accepts "c" or "f" as valid input;
            defaults to 'c'

        Returns:
            a numeric type of the temperature in the selected format.

        Examples:
            >>> convert_temperature('32F', 'c')
            0.0         
    """
    input_type = temperature[-1].lower()
    temperature = int(temperature[0:-1])
    if input_type == output_format:
        result = temperature
    elif input_type == 'f' and output_format == 'c':
        result = fahrenheit_to_celsius(temperature)
    elif input_type == 'c' and output_format == 'f':
        result = celsius_to_fahrenheit(temperature)
    else:
        result = None

    return result
