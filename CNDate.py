
import time
import calendar

ticks = time.time()
print(ticks)

localtime = time.localtime(time.time())
print(localtime)


localtime = time.asctime()
print(localtime)

localtime = time.localtime()

t1 = time.strftime('%Y-%m-%d %H-%M-%S', localtime)
print(t1)

t1 = time.strftime('%a-%b-%d %H-%M-%S', localtime)
print(t1)

m = calendar.month(2019, 9)
print(m)

print(time.process_time())
print(time.perf_counter())

print(time.timezone / 60 / 60)

print(calendar.isleap(2020))

