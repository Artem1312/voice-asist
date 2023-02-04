import time
import datetime

now = datetime.datetime.now()

print()
print( "Текущая дата и время с использованием метода str:")
print (str(now))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print (now.isoformat())

print(now.strftime("%H:%M"))
