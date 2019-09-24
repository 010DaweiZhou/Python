#!/usr/bin/python3

import time
import os
import random
import sys

class Server():
    usertime = 0

    def add(self):
        port = random.randint(11000, 20000)
        password = random.randint(100000, 999999)

        os.system('./addExcept ' + str(port) + " " + str(password))
        distmonth = time.localtime()[1] + self.usertime
        if distmonth > 12:
            distmonth -= 12
        
        with open('/root/ssr_record/record.txt', 'a', encoding='utf-8') as f:
            f.write('port=%d,password=%d,monthNow=%d,distMonth=%d,distday=%d\n' %
                    (port ,password ,time.localtime()[1] ,distmonth ,time.localtime()[2]))
        
        print('add user and write to file success !')
            

def main():
    ss = Server()
    if sys.argv[1] != None:
        ss.usertime = int(sys.argv[1])
    else:
        print('Month needed ! exit...')
        quit()
    
    print('Generating a user for %d month' % ss.usertime)
    time.sleep(1)
    ss.add()

main()

