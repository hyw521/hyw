# import os
# pid = os.fork()
# if pid < 0:
#     print('Error')
# elif pid == 0:
#     print('child process',os.getpid())
#     os._exit(5)
# else:
#     p,status = os.wait()
#     print('p:',p)
#     print('status:',status)
#     while True:
#         pass


import os
from time import sleep
def f1():
    for i in range(4):
        sleep(2)
        print('写代码')

def f2():
    for i in range(5):
        sleep(3)
        print('测代码')

pid = os.fork()
if pid < 0:
    print('error')
elif pid == 0:
    pid2 = os.fork()
    if pid2 == 0:
        f2()
    else:
        os._exit(0)

else:
    os.wait()
    f1()