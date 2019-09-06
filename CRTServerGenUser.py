import random
import sys

def addUser():
    port = random.randint(11000, 20000)
    passwd = random.randint(100000, 999999)

    crt.Screen.Send('cd /root/vpn/' + '\r')
    crt.Screen.WaitForString('#')

    crt.Screen.Send('bash ssr.sh' + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send('7' + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send('1' + '\r')
    crt.Screen.WaitForString(':')
    
    crt.Screen.Send(str(port) + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send(str(passwd) + '\r')
    crt.Screen.WaitForString('#')

    crt.Screen.Send('cd /' + '\r')
    crt.Screen.WaitForString('#')



def deleteUser(port):
    crt.Screen.Send('cd /root/vpn/' + '\r')
    crt.Screen.WaitForString('#')

    crt.Screen.Send('bash ssr.sh' + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send('7' + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send('2' + '\r')
    crt.Screen.WaitForString(':')
    
    crt.Screen.Send(str(port) + '\r')
    crt.Screen.WaitForString(':')

    crt.Screen.Send('cd /' + '\r')
    crt.Screen.WaitForString('#')



def main():

    crt.Screen.Synchronous = True

    deleteUser()
    addUser()

    crt.Screen.Synchronous = False


main()