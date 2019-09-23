
import time
import threading
import queue

threadLock = threading.Lock()

i = 0

def threadFun(threadname):
    global i
    while i < 10:
        threadLock.acquire()
        print(threadname + ' ' + str(i))
        i += 1
        threadLock.release()
        time.sleep(1)

def parseQueue():
    while workqueue.empty() == False :
        threadLock.acquire()
        result = workqueue.get()
        print(threading.currentThread().getName() + ' ' + str(result))
        threadLock.release()
        time.sleep(1)


class MyThread(threading.Thread):
    
    def __init__(self, threadId, threadName):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName

    def run(self):
        # threadFun(self.threadName)
        parseQueue()


# myThread1 = MyThread(1,'one')
# myThread1.start()

# myThread2 = MyThread(2, 'two')
# myThread2.start()

# myThread1.join()
# myThread2.join()

workqueue = queue.Queue(100)
list1 = list()

for num in range(100):
    list1.append((num))

threadLock.acquire()
for item in list1:
    workqueue.put(item)
threadLock.release()
del list1

mt1 = MyThread(1,'a')
mt2 = MyThread(2,'b')
mt3 = MyThread(3,'c')
mt4 = MyThread(4,'d')

mt1.start()
mt2.start()
mt3.start()
mt4.start()

mt1.join()
mt2.join()
mt3.join()
mt4.join()

print('exit...')


