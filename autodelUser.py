#!/usr/bin/python3

import os
import time
import re

delCommands = ['bash ssr.sh',
               '7'
               '2']

def main():

    while True:
        with open('record.txt', 'r', encoding='utf-8') as of,open('record.txt.back', 'w', encoding='utf-8') as nf:
                lines = of.readlines()
                if lines != None:
                    for line in lines:

                        #get the distMonth
                        month = re.search(r'(?<=distMonth=)(\d+)', line, re.I)
                        day = re.search(r'(?<=distday=)(\d+)', line, re.I)
                        port = re.search(r'(?<=port=)(\d+)', line, re.I)


                        #get distMonth in file 
                        month = month.group(1)
                        port = port.group(1)
                        day = day.group(1)

                        #get month now 
                        monthNow = str(time.localtime()[1])
                        dayNow = str(time.localtime()[2])

                        if month == monthNow and day == dayNow:
                            #delete port 
                            for command in delCommands:
                                os.system(command)
                                time.sleep(2)
                            os.system(port)
                            time.sleep(2)
                            print('delete port success!')
                        else:
                            nf.write(line)

        os.system('rm record.txt')
        os.system('cp record.txt.back record.txt')            
        time.sleep(60*60*24)

main()

