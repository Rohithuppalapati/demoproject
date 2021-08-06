import collections
import datetime

print(datetime.date.today())
print(datetime.time(5,45,2))
print(datetime.timedelta(1,hours=20,minutes=14,seconds=24))


word='hello how are you today'
count=collections.Counter(word)
print(count)
