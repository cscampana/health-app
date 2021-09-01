import constant
import math
import argparse


def check_is_valid_number(*args):
    for arg in args:
        try:
            if arg.isdigit():
                return True
            elif float(arg):
                return True
        except ValueError:
            SystemExit("Not a digit " + str(arg))


def calculate_macros(carbs, proteins, fats):
    if check_is_valid_number(carbs, proteins, fats):
        return constant.CALORIES_CARBS * float(carbs) + constant.CALORIES_PROTEIN * float(
            proteins) + constant.CALORIES_FAT * float(fats)


def calculate_bmi_metric(weight, height):
    if check_is_valid_number(weight, height):
        return (float(weight) / math.pow(float(height), 2)) * 10000


def convert_imperial_metric(weight, height):
    if check_is_valid_number(weight, height):
        return constant.LBS_TO_KGS * float(weight), constant.IN_TO_CM * float(height)


def menu_no_commands():
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
            height, weight = convert_imperial_metric(weight, height)
        elif system_choice.upper() == "M":
            height = input(constant.METRIC_HEIGHT)
            weight = input(constant.METRIC_WEIGHT)
        else:
            print(constant.CORRECT_INPUT_SYSTEM)
            main()
        print(constant.RESULT_BMI + str(calculate_bmi_metric(weight, height)))


def main():
    cli_arguments = argparse.ArgumentParser(description=constant.DESCRIPTION_OVERALL)
    cli_arguments.add_argument(constant.OPTION_MACRO, constant.OPTION_MACRO_SHORT, action='store', type=str, nargs=3,
                               help=constant.DESCRIPTION_MACRO, metavar="Amount")
    cli_arguments.add_argument(constant.OPTION_BMI, constant.OPTION_BMI_SHORT, action='store', type=str, nargs=2,
                               help=constant.DESCRIPTION_BMI, metavar="Measurements")
    cli_arguments.add_argument(constant.OPTION_IMPERIAL, action='store_true',
                               help=constant.DESCRIPTION_IMPERIAL)
    args, leftover = cli_arguments.parse_known_args()
    if args.MACRO is not None and len(args.MACRO) == 3:
        print(constant.RESULT_MACRO + str(calculate_macros(args.MACRO[0], args.MACRO[1], args.MACRO[2])) + " calories")
    if args.BMI is not None and len(args.BMI) == 2:
        if args.i is True:
            kg, cm = convert_imperial_metric(weight=args.BMI[0], height=args.BMI[1])
            print(constant.RESULT_BMI + str(calculate_bmi_metric(weight=str(kg), height=str(cm))))
        else:
            print(constant.RESULT_BMI + str(calculate_bmi_metric(weight=args.BMI[0], height=args.BMI[1])))
    else:
        menu_no_commands()


if __name__ == '__main__':
    main()
