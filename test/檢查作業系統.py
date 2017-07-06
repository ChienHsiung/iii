from sys import platform as pf

if pf == 'win32':
    print('Windows')
elif pf == 'linux':
    print('LINUX')