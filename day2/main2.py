with open('input2.txt') as file:
    d2_input = file.read().splitlines()   # open without /n

games = [line.replace('Game ', '').split(': ') for line in d2_input]
max_red, max_green, max_blue = 12, 13, 14
possible_games, powers = 0, 0

for game in games:
    max_drawn_red, max_drawn_green, max_drawn_blue = 0, 0, 0
    draws = game[1].split('; ')
    for draw in draws:
        cubes = draw.split(', ')
        for cube in cubes:
            amount = int(cube.split(' ')[0])
            colour = cube.split(' ')[1]
            if colour == 'red':
                max_drawn_red = max(max_drawn_red, amount)
            elif colour == 'green':
                max_drawn_green = max(max_drawn_green, amount)
            else:
                max_drawn_blue = max(max_drawn_blue, amount)
    if not (max_drawn_red > max_red or max_drawn_green > max_green or max_drawn_blue > max_blue):
        possible_games += int(game[0])
    powers += max_drawn_red * max_drawn_green * max_drawn_blue

# puzzle 1:
print('no of possible games:', possible_games)

# puzzle 2:
print('sum of powers:', powers)
