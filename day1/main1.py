with open('input1.txt') as file:
    d1_input = file.read().splitlines()   # open without /n


def puzzle1():
    calibration_values = [[value for value in line if value.isnumeric()] for line in d1_input]
    sum_of_calibration_values = sum(int(digits[0] + digits[-1]) for digits in calibration_values)
    print('sum of all calibration values:', sum_of_calibration_values)


puzzle1()
