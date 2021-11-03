from tabulate import tabulate
from random import randint
from sys import exit
import os
import copy

clear = lambda: os.system('cls')

Count = 0
Field = []

Size = 6
Mines = 3
StartCount = 0

for r in range(0, Size):
    Field.append([])
    for c in range(0, Size):
        Field[r].append(0)

FieldX = copy.deepcopy(Field)

for r in range (0,len(Field)):
    for c in range (0,len(Field)):
        FieldX[r][c] = "X"

while(StartCount < Mines):
    Randr = randint(0,Size - 1)
    Randc = randint(0,Size - 1)
    if(Field[Randr][Randc] != -1):
        Field[Randr][Randc] = -1
        StartCount += 1

for r in range(0,len(Field)):
    for c in range(0,len(Field)):
        if(Field[r][c] != -1):
            if(c-1 != -1):
                if(Field[r][c-1] == -1):
                    Field[r][c] += 1

            if(c+1 != len(Field)):
                if(Field[r][c+1] == -1):
                    Field[r][c] += 1

            if(r-1 != -1):
                if(Field[r-1][c] == -1):
                    Field[r][c] += 1

            if(r+1 != len(Field)):
                if(Field[r+1][c] == -1):
                    Field[r][c] += 1

            if(r-1 != -1 and c-1 != -1):
                if(Field[r-1][c-1] == -1):
                    Field[r][c] += 1

            if(r-1 != -1 and c+1 != len(Field)):
                if(Field[r-1][c+1] == -1):
                    Field[r][c] += 1

            if(r+1 != len(Field)  and c-1 != -1):
                if(Field[r+1][c-1] == -1):
                    Field[r][c] += 1

            if(r+1 != len(Field) and c+1 != len(Field)):
                if(Field[r+1][c+1] == -1):
                    Field[r][c] += 1

clear()

print(tabulate(FieldX, tablefmt='plain'))

UserInput = input()

UserR = int(list(UserInput)[0]) - 1
UserC = int(list(UserInput)[1]) - 1
UserA = list(UserInput)[2]

while(True):
    if(UserA == "c"):
        if(Field[UserR][UserC] == -1):
            Status = "LOSE"
            break
        else:
            FieldX[UserR][UserC] = Field[UserR][UserC]
    if(UserA == "f"):
            FieldX[UserR][UserC] = "F"

    for r in range (0,len(Field)):
        for c in range (0,len(Field)):
            if(Field[r][c] == -1 and FieldX[r][c] == "F"):
                Count += 1

    if(Count == Mines):
        Status = "WIN"
        break
    else:
        Count = 0

    clear()

    print(tabulate(FieldX, tablefmt='plain'))

    UserInput = input()

    UserR = int(list(UserInput)[0]) - 1
    UserC = int(list(UserInput)[1]) - 1
    UserA = list(UserInput)[2]

clear()
print(tabulate(Field, tablefmt='plain'))

if(Status == "WIN"):
    print("Victory!")
elif(Status == "LOSE"):
    print("Dead!")
