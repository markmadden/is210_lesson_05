#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 Code."""


def celsius_to_fahrenheit(temperature):

    fahren = float(9.0 * temperature / 5.0 + 32.0)

    return fahren

def fahrenheit_to_celsius(temperature):

    celsi = float(5.0 * (temperature - 32.0) / 9.0)

    return celsi

def convert_temperature(temperature, output_format='c'):

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
