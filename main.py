#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HealthApp

In this application the user has two options: Provide the carbohydrates, proteins, and fats in grams from a food to
calculate the calories it provides, or providing a weight and a height, in imperial or metric system, calculate their
BMI.

The program can be executed from the command line using arguments or from a text interface.

To use the text interface, simply run the program. Now to use the command line argument, the user needs to provide
the following options:
Macro calculator:
--MACRO carbohydrates proteins fats
-m carbohydrates proteins fats
Body mass index:
--BMI weight height
-b weight height
-i (flag to indicate the program to use the imperial system)

Use the flag -h for more help regarding command line arguments.
"""

# Libraries
import sys
import constant
import math
import argparse

__author__ = "Caike Salles Campana"
__license__ = "CC0 1.0 Universal (CC0 1.0) Public Domain Dedication"
__version__ = "1.0"
__maintainer__ = "Caike Salles Campana"
__email__ = "csallesc@ucsd.edu"
__status__ = "Development"


def check_is_valid_number(*args):
    """
    Using a pointer variable, checks to see if the number(s) is(are) valid. Throws an ValueError exception
    and exits the program otherwise.
    :param args: numbers to be checked.
    :return: a boolean true in case it is a number.
    """
    for arg in args:
        try:
            if arg.isdigit():
                return True
            elif float(arg):
                return True
        except ValueError:
            SystemExit("Not a digit " + str(arg))


def calculate_macros(carbs, proteins, fats):
    """
    Calculate the calories per gram of each macronutrient. For carbohydrates, it is considered 4 calories,
    protein 4 calories, and fat 9 calories.
    :param carbs: amount of carbohydrates in the food.
    :param proteins: amount of proteins in the food.
    :param fats: amount of fat in the food.
    :return: the total calorie count of the food.
    """
    if check_is_valid_number(carbs, proteins, fats):
        return constant.CALORIES_CARBS * float(carbs) + constant.CALORIES_PROTEIN * float(
            proteins) + constant.CALORIES_FAT * float(fats)


def calculate_bmi_metric(weight, height):
    """
    Calculates the body mass index in metric values. Using the formula (weight/height^2)*10000.
    :param weight: weight of the person
    :param height: height of the person
    :return: the body mass index
    """
    if check_is_valid_number(weight, height):
        return (float(weight) / math.pow(float(height), 2)) * 10000


def convert_imperial_metric(weight, height):
    """
    Converts the weight and height from imperial to metric. It uses two multiplication constants to achieve the
    desired result. The conversion value between pounds and kilograms is 0.45359237 kg per each pound, and the
    value conversion between inches and centimeters is 2.54 centimeters for each inch.
    :param weight: the weight in pounds.
    :param height: the height in inches.
    :return: a tuple containing the values in metric system respectively.
    """
    if check_is_valid_number(weight, height):
        return constant.LBS_TO_KGS * float(weight), constant.IN_TO_CM * float(height)


def menu_no_commands():
    """
    A simple menu to allow for the user, a more interactive experience with the program.
    """
    print(constant.WELCOME_MSG)
    option = input(constant.OPTIONS)
    # To be update according PEP 634 implementation of the Structural Pattern Matching. Planned Oct/2021
    if int(option) == 1:
        print(constant.OPTION_MACROS)
        carbs = input(constant.CARB_AMOUNT)
        protein = input(constant.PROTEIN_AMOUNT)
        fat = input(constant.FAT_AMOUNT)
        total = calculate_macros(carbs, protein, fat)
        print(constant.RESULT_MACRO + str(total) + " calories")
    if int(option) == 2:
        height = 0
        weight = 0
        system_choice = input(constant.IMPERIAL_OR_METRIC)
        if system_choice.upper() == "I":
            height = input(constant.IMPERIAL_HEIGHT)
            weight = input(constant.IMPERIAL_WEIGHT)
            weight, height = convert_imperial_metric(weight, height)
        elif system_choice.upper() == "M":
            height = input(constant.METRIC_HEIGHT)
            weight = input(constant.METRIC_WEIGHT)
        else:
            print(constant.CORRECT_INPUT_SYSTEM)
            main()
        print(constant.RESULT_BMI + str(calculate_bmi_metric(str(weight), str(height))))


def main():
    """
    The main method parses the arguments and if there are none, calls the method menu_no_commands()
    """
    cli_arguments = argparse.ArgumentParser(description=constant.DESCRIPTION_OVERALL)
    cli_arguments.add_argument(constant.OPTION_MACRO, constant.OPTION_MACRO_SHORT, action='store', type=str, nargs=3,
                               help=constant.DESCRIPTION_MACRO, metavar="Amount")
    cli_arguments.add_argument(constant.OPTION_BMI, constant.OPTION_BMI_SHORT, action='store', type=str, nargs=2,
                               help=constant.DESCRIPTION_BMI, metavar="Measurements")
    cli_arguments.add_argument(constant.OPTION_IMPERIAL, action='store_true',
                               help=constant.DESCRIPTION_IMPERIAL)
    args, leftover = cli_arguments.parse_known_args()
    if len(sys.argv) == 1:
        menu_no_commands()
    elif args.MACRO is not None and len(args.MACRO) == 3:
        print(constant.RESULT_MACRO + str(calculate_macros(args.MACRO[0], args.MACRO[1], args.MACRO[2])) + " calories")
    if args.BMI is not None and len(args.BMI) == 2:
        if args.i is True:
            kg, cm = convert_imperial_metric(weight=args.BMI[0], height=args.BMI[1])
            print(constant.RESULT_BMI + str(calculate_bmi_metric(weight=str(kg), height=str(cm))))
        else:
            print(constant.RESULT_BMI + str(calculate_bmi_metric(weight=args.BMI[0], height=args.BMI[1])))


if __name__ == '__main__':
    main()
