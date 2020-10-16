import numpy as np
import random
from time import sleep

WIDTH, HEIGHT = 10, 10
field = np.zeros((WIDTH, WIDTH), int)


"""
Rules:
---------
POV: 3 (Eagle)
if neighbors includes one 2:
    move to the 2's position
else if neighbors includes more than one 2:
    move to the first 2 in the neighbors
else if neighbors does not include a 2:
    turn self to 0 (dies to hunger)
---------
POV: 2 (Cat)
if neighbors includes one 1:
    move to the 1's position
else if neighbors includes more than one 1:
    move to the first 1 in the neighbors
else if neighbors does not include a 1:
    turn self to 0 (dies to hunger)
---------
POV: 1 (Mouse)
if neighbors includes one 0:
    move to the 0's position
else if neighbors includes more than one 0:
    move to the first 0 in the neighbors


"""


def placeAnimals():
    for row in range(HEIGHT):
        for column in range(WIDTH):
            field[row][column] = random.choice([1, 2, 3])


def getNeighbors():
    for row in range(HEIGHT):
        for column in range(WIDTH):

            positions = {
                'above_left': (row - 1, column - 1),
                'above': (row - 1, column),
                'above_right': (row - 1, column + 1),

                'left': (row, column - 1),
                'right': (row, column + 1),

                'below_left': (row + 1, column - 1),
                'below': (row + 1, column),
                'below_right': (row + 1, column + 1)
            }
            neighbors = []
            for position, indexes in positions.items():
                currentNum = field[row][column]
                try:
                    if indexes[0] >= 0 and indexes[1] >= 0:
                        neighbor = field[indexes[0]][indexes[1]]
                        if currentNum == 3:
                            if neighbor == 2:
                                field[indexes[0]][indexes[1]] = 3
                                field[row][column] = 0

                            elif neighbor == 0:
                                field[indexes[0]][indexes[1]] = 3
                                field[row][column] = 0
                            else:
                                field[row][column] = 0
                        elif currentNum == 2:
                            if neighbor == 1:
                                field[indexes[0]][indexes[1]] = 2
                                field[row][column] = 0
                            elif neighbor == 0:
                                field[indexes[0]][indexes[1]] = 2
                                field[row][column] = 0
                            else:
                                field[row][column] = 0
                        elif currentNum == 1:
                            if neighbor == 0:
                                field[indexes[0]][indexes[1]] = 1
                                field[row][column] = 0
                            else:
                                field[row][column] = 0
                        neighbors.append(neighbor)
                except IndexError:
                    pass
    print(field)
    # return neighbors


def main():
    placeAnimals()
    print(field)
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    sleep(1)
    getNeighbors()
    


main()
