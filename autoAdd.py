#!/usr/bin/python3

import time
import os
import random
import sys

class Server():
    usertime = 0
    username = ''

    def add(self):
        port = random.randint(11000, 20000)
        password = random.randint(100000, 999999)

        os.system('./addExcept ' + str(port) + " " + str(password))

        distYear = time.localtime()[0]
        distmonth = time.localtime()[1] + self.usertime

        while distmonth > 12:
            distmonth -= 12
            distYear += 1

        with open('/root/ssr_record/record.txt', 'a', encoding='utf-8') as f:
            f.write('user=%s,port=%d,password=%d,disYear=%d,distMonth=%d,distday=%d\n' %
                    (self.username ,port ,password ,distYear ,distmonth ,time.localtime()[2]))
        
        print('add user and write to file success !')
            

def main():
    ss = Server()
    argc = len(sys.argv) - 1

    if argc == 0:
        print('<cmd> <months> <username>...')
        quit()

    if argc >= 1 and sys.argv[1] != None:
        ss.usertime = int(sys.argv[1])
    else:
        print('Month needed ! exit...')
        quit()
    
    if argc == 2 and sys.argv[2] != None:
        ss.username = sys.argv[2]
    else:
        print('no username... but add operation is normal...')

    print('Generating a user for %d month' % ss.usertime)
    time.sleep(1)
    ss.add()

main()

