# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 15:02:00 2021

@author: xzy
"""

list=eval(input('Enter List :'))
print('METHODS\n
      1.append()\n
      2.clear()\n
      3.copy()\n
      4.count()\n
      5.extend()\n
      6.index()\n
      7.insert()\n
      8.pop()\n
      9.remove()\n
      10.reverse()\n
      11.sort()')
m=('Enter method no. that you want to execute:')      
if  m==1:
    a=input('Enter element to add ')
    list.append(a)
    print(list)
if m==2:
    list.clear()
    print(list)
if m==3:
   print(list.copy())
if m==4:
   print(list.count()) 
if m==5:
   b=eval(input('enter elements to be added:'))
if m==6:
   c=input('Enter element from list to find index:'))
   print(list.index(c))
if m==7:
   d=input('enter element to be inserted:')
   e=int(input('Enter position of element to be inserted'))
   list.insert(d,e)
   print(list)
if m==8:
   e=('enter element to be popped:')
   list.pop(d)
   print(list)
if m==9:
   f=input('Enter item to be removed:')
   list.remove(f)
if m==10:
   print(list.reverse())
if m==11:
    print(list.sort())
    
else:
    print('method number not found')
                                                                                 