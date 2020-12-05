import random
import math


def saveListToFile(list, fileName: str):
    file = open(fileName, 'a')

    for item in list:
        percent: int = math.trunc(float(item) * 100)
        text: str = item + ' ; ' + str(percent) + '%\n'
        file.write(text)
    file.close()


numbers = []
numbersCount: int = int(input('Podaj ilość liczb jakie chcesz wprowadzić: '))
currentNumber: int = 0

while currentNumber < numbersCount:
    numbers.append(format(random.random(), '.5f'))
    currentNumber += 1

sortedNumbers = sorted(numbers, key=float)
saveListToFile(sortedNumbers, 'percent.txt')
