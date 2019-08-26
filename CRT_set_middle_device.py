import time

'''
    1/0/5               1/1/1      1/1/4                  1/1/4
    R1-------------------------R2----------------------------R3
20.0000.0000.0002       10.0000.0000.0001             10.0000.0000.0003
  L1-2(H3C)                   L1-2                           L1

'''


def mySend(command):
    crt.Screen.Send(command + '\r')
    crt.Screen.WaitForString('Hios')


commands_create_instance = 'isis instance 1', \
    'net entity 10.0000.0000.0001.00', \
    'exit',\
    'interface gigabitethernet 1/1/1', \
    'isis enable instance 1',\
    'isis enable ipv6 instance 1', \
    'exit', \
    'interface gigabitethernet 1/1/4', \
    'isis enable instance 1',\
    'isis enable ipv6 instance 1', \
    'exit'

commands_set_interface_cost = 'interface gigabitethernet 1/1/1', \
    'isis cost 20', \
    'exit', \
    'interface gigabitethernet 1/1/4', \
    'isis cost 30', \
    'exit'

commands_import_isis = 'isis 1', \
    'address-family ipv6', \
    'import-route isisv6 level-2 into level-1',\
    'address-family ipv4',\
    'import-route isis level-2 into level-1', \
    'end'

commands_import_static = 'isis 1', \
    'address-family ipv6', \
    'import-route static level-1-2',\
    'address-family ipv4',\
    'import-route static level-1-2', \
    'end'

def main():

    crt.Screen.Synchronous = True

    for command in commands_create_instance:
        mySend(command)

    for command in commands_set_interface_cost:
        mySend(command)

    for command in commands_import_isis:
        mySend(command)

    for command in commands_import_static:
        mySend(command)

    crt.Screen.Synchronous = False


main()
