import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
t=time.localtime()
print('time.asctime(t): %s '%time.asctime(t))
print(time.ctime())
a=time.strftime('%Y/%m/%d %H:%M:%S')
print(a)