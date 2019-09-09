
import pickle
import os
file = open('record.txt', 'w+')

file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.write('hello world!\n')
file.flush()
file.close()

file = open('record.txt', 'r')
filelist = list(file)
print(filelist)
file.close()

print(os.getcwd())
os.chdir('F:' + os.sep)

if os.path.exists('test') == False:
    os.mkdir('test')

os.chdir(r'.\test')
print(os.getcwd())

dirs = os.listdir()
print(dirs)

if os.path.exists('test') == False:
    os.mkdir('test')

for i in os.walk(r'F:' + os.sep + 'test'):
    print(i)

for dir in os.listdir():
    print(dir)
    if dir == 'test':
        os.rmdir(dir)
        print('remove ' + dir + ' successful!')
    elif dir == 'a':
        os.removedirs(r'.\a\b\c')
    else:
        pass

os.chdir(r'/..')
print(os.getcwd())
newname = 'a'
os.rename('test', newname)
os.rmdir(newname)
print(os.name)
print(os.curdir)

# os.system('calc')

os.chdir('F:'+os.sep+'Github'+os.sep+'Python')
currentPath = os.getcwd()
print(os.path.dirname(currentPath))
print(os.path.basename(currentPath))
print(os.listdir('.'))

if os.path.exists('test.txt') == False:
    os.rename('record.txt', 'test.txt')

print(os.path.getsize('test.txt'))


pickle_file = open('list.pkl', 'wb')

list1 = [1, 2, 3, 4, 5, 6, 7]

if(pickle_file.writable()):
    pickle.dump(list1, pickle_file, -1)

pickle_file.close()

del pickle_file
del list1

pickle_file = open('list.pkl', 'rb')
list1 = pickle.load(pickle_file)
print(list1)

