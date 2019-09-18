
def mySend(command):
    crt.Screen.Send(command + '\r')
    crt.Screen.WaitForString('[')
    # crt.Screen.WaitForString('H')


def main():

    crt.Screen.Synchronous = True

    for i in range(500,700):
        mySend('undo ipv6 route-static 9999::' + str(i) + ' 128 NULL 0 ')
        # mySend('ipv6 route 9999::' + str(i) + '/128 blackhole ')

    crt.Screen.Synchronous = False


main()