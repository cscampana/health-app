import math

import constant


def check_is_valid_number(*args):
    for arg in args:
        if not arg.isnumeric():
            raise SyntaxError("Not a digit " + arg)


def calculate_macros(carbs, proteins, fats):
    check_is_valid_number(carbs, proteins, fats)
    return constant.CALORIES_CARBS * float(carbs) + constant.CALORIES_PROTEIN * float(
        proteins) + constant.CALORIES_FAT * float(fats)


def calculate_bmi_metric(weight, height):
    check_is_valid_number(weight, height)
    return (float(weight) / math.pow(float(weight), 2)) * 10000


def convert_imperial_metric(weight, height):
    check_is_valid_number(weight, height)
    return constant.LBS_TO_KGS * float(weight), constant.IN_TO_CM * float(weight)


def main():
    print(constant.WELCOME_MSG)
    print(constant.OPTIONS)
    option = input()
    if option is 1:



if __name__ == '__main__':
    main()
