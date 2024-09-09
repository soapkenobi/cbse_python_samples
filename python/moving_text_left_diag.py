import os
import time
width = os.get_terminal_size()[0]
s = input()
left_diag = True
i = 0
while True:
    for j in range(i):
        print()
    print(' ' * i, s)
    time.sleep(0.05)
    os.system("clear")
    if i>os.get_terminal_size()[1]:
        break
    i+=1
