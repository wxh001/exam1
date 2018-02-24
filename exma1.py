"""
import sys
ss  = sys.path
aa = '/storage/emulated/0/python'
ss.append(aa)
from os import system
system('sh')
ls
cd /storage/emulated/0/python
ls
"""
from os import system
pinghead = 'ping -c 8 '
print('%%%%%============================%%%%')
print('The program func is ping ip or domain\n')
print("For  :   ping - c 8 192.168.1.1\n ")
print("You 'll enter :  192.168.1.1 \n And it will working well\n")
print("And press  'q' to quit the program\n")
print('%%%%%===========================%%%%%')
cont=input('enter any key to continue......\n')
if cont == 'q':  pass
else :
   while True:
      if cont == 'q' : break
      cont = input('enter a ip or domain or "q" to exit\n ip: ')
      kk = pinghead + cont
      system(kk)
      print('\n\n')
print('ping in phone \n')
print ('******   over    ******   \n')
