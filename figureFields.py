import math


def getCircleArea(radius: float):
    return math.pi * math.pow(radius, 2)


def getTriangleArea(height: float, sideA: float):
    return 0.5 * sideA * height


def getRectangleArea(sideA: float, sideB: float = None):
    if sideB is None:
        return math.pow(sideA, 2)
    else:
        return sideA * sideB


print('Witaj w kalkulatorze pól figur geometrycznych.')

try:
    area: float
    idFigury = int(
        input('Wybierz figurę geometryczną:\n1. Koło\n2. Trójkąt\n3. Prostokąt\n'))

    if idFigury == 1:
        radius: float = float(input('Podaj długość promienia koła: '))

        area = getCircleArea(radius)
        print('Pole koła wynosi', area, 'jednostek kwadratowych')
    elif idFigury == 2:
        sideA: float = float(input('Podaj długość boku A: '))
        height: float = float(input('Podaj wysokość trójkąta: '))

        area = getTriangleArea(height, sideA)
        print('Pole trójkąta wynosi', area, 'jednostek kwadratowych')
    elif idFigury == 3:
        sideA: float = float(input('Podaj długość boku A: '))
        sideB: float = float(input('Podaj długość boku B: '))

        area = getRectangleArea(sideA, sideB)
        print('Pole prostokąta wynosi', area, 'jednostek kwadratowych')
    else:
        print('Wprowadzono nieprawidłowy nr operacji')
except:
    print('Wprowadzono nieprawidłowe dane.')
