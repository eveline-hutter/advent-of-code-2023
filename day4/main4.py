with open('input4.txt') as file:
    d4_input = file.read().splitlines()   # open without /n

cards = [line.split(': ')[1].split(' | ') for line in d4_input]
winning_numbers = [card[0].split() for card in cards]
elfs_numbers = [card[1].split() for card in cards]
points = 0

for i in range(len(cards)):
    matching_numbers = 0
    for number in winning_numbers[i]:
        if elfs_numbers[i].__contains__(number):
            matching_numbers += 1
    if matching_numbers > 0:
        points += 2 ** (matching_numbers - 1)

# puzzle 1:
print('points:', points)
