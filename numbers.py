numbers = []

try:
    command: str = ''

    while command != 'exit':
        command = input('Podaj liczbę: ')
        if command != 'exit':
            number: int = int(command)
            numbers.append(number)

    for number in numbers:
        print(str(number))

except:
    print('Podałeś', len(numbers), 'liczb/-y. Dalej się nie bawię')
