with open('input6.txt') as file:
    d6_input = [line.split() for line in file.read().splitlines()]   # open without /n


def puzzle1():
    no_of_races = len(d6_input[0]) - 1
    times = [int(d6_input[0][i]) for i in range(1, no_of_races + 1)]
    distances = [int(d6_input[1][i]) for i in range(1, no_of_races + 1)]
    total_ways_to_win = 1

    for i in range(no_of_races):
        record = distances[i]
        ways_to_win = 0
        time = times[i]
        for speed in range(1, time):
            moving_time = time - speed
            distance = speed * moving_time
            if distance > record:
                ways_to_win += 1
        total_ways_to_win *= ways_to_win

    print('multiply of number of ways to beat the record:', total_ways_to_win)


def puzzle2():
    no_of_races = len(d6_input[0]) - 1
    times = [d6_input[0][i] for i in range(1, no_of_races + 1)]
    distances = [d6_input[1][i] for i in range(1, no_of_races + 1)]
    time, record = '', ''
    for i in range(len(times)):
        time += times[i]
        record += distances[i]

    time, record = int(time), int(record)
    ways_to_win = 0
    for speed in range(1, time):
        moving_time = time - speed
        distance = speed * moving_time
        if distance > record:
            ways_to_win += 1

    print('ways to win:', ways_to_win)


puzzle1()
puzzle2()
