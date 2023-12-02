with open('input1.txt') as file:
    d1_input = file.read().splitlines()   # open without /n


def puzzle1():
    calibration_values = [[value for value in line if value.isnumeric()] for line in d1_input]
    sum_of_calibration_values = sum(int(digits[0] + digits[-1]) for digits in calibration_values)
    print('sum of all calibration values:', sum_of_calibration_values)


def puzzle2():
    digit_letters = [['one', 'on1e'], ['two', 't2wo'], ['three', 'thr3ee'],
                     ['four', 'fo4ur'], ['five', 'fi5ve'], ['six', 'si6x'],
                     ['seven', 'se7ven'], ['eight', 'ei8ght'], ['nine', 'ni9ne']]
    digitised_input = []
    for line in d1_input:
        for digit in digit_letters:
            if line.__contains__(digit[0]):
                line = line.replace(digit[0], digit[1])
        digitised_input.append(line)
    calibration_values = [[value for value in line if value.isnumeric()] for line in digitised_input]
    sum_of_calibration_values = sum(int(digits[0] + digits[-1]) for digits in calibration_values)
    print('sum of all calibration values:', sum_of_calibration_values)


puzzle1()
puzzle2()
