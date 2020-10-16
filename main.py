import numpy as np
import random
from time import sleep

WIDTH, HEIGHT = 15, 15
field = np.zeros((WIDTH, WIDTH), int)



# spawns animals
def placeAnimals():
    for row in range(HEIGHT):
        for column in range(WIDTH):
            field[row][column] = random.choice([1, 2, 3])

#gets neighbors and applies rules
def updateField():
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



def main():
    placeAnimals()
    print(field)
    sleep(1)
    for i in range(WIDTH): # to progressively see the simulation take place
        updateField()
        sleep(1)



main()
