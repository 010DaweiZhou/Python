#!/usr/bin/python3

import os
import time
import re


def main():

    while True:
        with open('/root/ssr_record/record.txt', 'r', encoding='utf-8') as of,open('/root/ssr_record/record.txt.back', 'w', encoding='utf-8') as nf:
                lines = of.readlines()
                if lines != None:
                    for line in lines:

                        #get the dist Y-M-D
                        year = re.search(r'(?<=disYear=)(\d+)',line,re.I)
                        month = re.search(r'(?<=distMonth=)(\d+)', line, re.I)
                        day = re.search(r'(?<=distday=)(\d+)', line, re.I)
                        port = re.search(r'(?<=port=)(\d+)', line, re.I)


                        #get distMonth in file 
                        year = year.group(1)
                        month = month.group(1)
                        port = port.group(1)
                        day = day.group(1)

                        #get month now 
                        yearNow = str(time.localtime()[0])
                        monthNow = str(time.localtime()[1])
                        dayNow = str(time.localtime()[2])

                        if year == yearNow and month == monthNow and day == dayNow:
                            #delete port 
                            os.system('./delExcept ' + str(port))
                            print('delete port success!')
                        else:
                            nf.write(line)

        os.system('rm /root/ssr_record/record.txt')
        os.system('cp /root/ssr_record/record.txt.back /root/ssr_record/record.txt')            
        time.sleep(60*60*24)

main()
