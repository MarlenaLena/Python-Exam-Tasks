import time
import math

file = open('logs.txt', 'a')
userSeconds: int = int(input('Podaj przez ile sekund ma działać ten skrypt: '))

for i in range(userSeconds):
    dateAndTime: str = time.strftime('%d %b %Y | %H:%M:%S')
    timestamp: int = math.trunc(time.time())
    dateTimeInfo: str = str(i + 1) + ' | ' + dateAndTime + \
        ' | ' + str(timestamp) + '\n'
    file.write(dateTimeInfo)
    time.sleep(1)

file.close()
