import time
from datetime import datetime

d = datetime.now()
t = time.strftime('%d-%m-%YT%H:%M:%S:{0!s:.5}'.format(d.microsecond))
s = '4323'
p = 'kis'
o = 'asdkjaklsfdjbkasfbkadbfkbskdgbksdfnglkndsfgklnsdfkgnksdjfngknsdfkgnd kdsjg'

for i in range(100):

  print('{0:<20}   {1:<6}   {2:<6}   {3:<20}'.format(t, s, p, o))