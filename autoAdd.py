#!/usr/bin/python3

import time
import os
import random
import sys

class Server():
    usertime = 0

    addCommands = ['bash ssr.sh',
                   '7'
                   '1']

    def add(self):

        for command in self.addCommands:
            os.system(command)
            time.sleep(2)
        port = random.randint(11000, 20000)
        password = random.randint(100000, 999999)
        os.system('port')
        time.sleep(2)
        os.system('password')
        time.sleep(2)

        with open('record.txt', 'a', encoding='utf-8') as f:
            f.write('port=%d,password=%d,monthNow=%d,distMonth=%d,distday=%d\n' %
                    (port, password, time.localtime()[1] ,time.localtime()[1] + self.usertime,time.localtime()[2]))
        
        print('add user and write to file success !')
            

def main():
    ss = Server()
    if sys.argv[1] != None:
        ss.usertime = int(sys.argv[1])
    else:
        ss.usertime = 11
    
    print('Generate a user for %d month' % ss.usertime)
    time.sleep(1)
    ss.add()
    

main()

