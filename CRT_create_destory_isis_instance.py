import time

def mySend(command):
    crt.Screen.Send(command + '\r')
    crt.Screen.WaitForString('Hios')


def main():
    commands = 'isis instance 1', \
            'net entity 10.0000.0000.0001.00', \
            'exit',\
            'interface g 1/1/1', \
            'isis enable instance 1',\
            'isis enable ipv6 instance 1', \
            'exit', \
            'interface g 1/1/4', \
            'isis enable instance 1',\
            'isis enable ipv6 instance 1', \
            'exit',\

    crt.Screen.Synchronous = True
    
    for i in range(100):
        for command in commands:
            mySend(command)
        time.sleep(30)
        mySend('no isis instance 1')

    crt.Screen.Synchronous = False


main()
