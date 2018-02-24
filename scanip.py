"""
scanip.py in "/storage/emulated/0/python"
pyhon or Qpython or Qpython3
import sys
ss = sys.path
aa = '/storage/emulated/0/python'
ss.append(aa)

import scanip
"""
from os import system
pinghead = 'ping -c 1 '
cacheip = []
print('%%%%%============================%%%%')
print('The program func is scan lan ip \n')
print("For  enter:  192.168\n ")
print("Or for enter :  172.16 networt adf\n")
print("And .1.xxx for host number\n")
print("And press  'q' to quit the program\n")
print('%%%%%===========================%%%%%')
cont=input('enter any key to continue......\n')
if cont == 'q':  pass
else :
   while True:
      if cont == 'q' : break
      cont = input('enter network add or "q" to exit\n net: ')
      if cont == 'q' : break
      host1 = input('enter host1 num \n host1:')
      host2 = input('enter host2 num \n host2:')
      for i in range(int(host2)):
         cont1 = cont + '.' + host1+ '.' + str(i+1)
         kk = pinghead + cont1
         back = system(kk)
         if not back :
            cacheip.append(cont1)
      for j in cacheip:
         print('ip %s is active' % j)
      print('\n\n')
print('ping in phone \n')
print ('******   over    ******   \n')
