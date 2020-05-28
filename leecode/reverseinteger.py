# -*- coding: utf-8 -*-
"""
Created on Wed May 27 23:55:58 2020

@author: user
"""


def reverse1(x):
    if x > 0: 
        y = list(str(x))
        y.reverse()
        z= ''.join(x for x in y)
        return (int(z))
    if x ==  0: 
        return 0 
    else:
        y = list(str(abs(x)))
        y.reverse()
        z= ''.join(x for x in y)
        return (- int(z))
            
#%%
reverse1(-120)

#%%
class Solution:
    def reverse1(x):
        if x > 0: 
            y = list(str(x))
            y.reverse()
            z= ''.join(x for x in y)
            return (int(z))
        if x ==  0: 
            return 0 
        else:
            y = list(str(abs(x)))
            y.reverse()
            z= ''.join(x for x in y)
            return (- int(z))

#%%
x= 123 
stringx = str(x)
y = list(stringx)
y.reverse()
print(y)
z= ''.join(x for x in y)
print(int(z))


#%%
x= 123
stringx = str(x)
y = list(stringx)
y.reverse()
print(y)
#%%
y.reverse()
print(y)
#%%
z= ''.join(x for x in y)
print(int(z))
#%%
1534236469 > 2147483647

#%% submit version 
def reverse(x):
        if x > 0: 
            y = list(str(x))
            y.reverse()
            z= ''.join(x for x in y)
            if int(z) <= (2**31-1):
                return (int(z))
            else: 
                return 0
        if x ==  0: 
            return 0 
        if x < 0 :
            y = list(str(abs(x)))
            y.reverse()
            z= ''.join(x for x in y)
            if int(z) <= (2**31-1):
                return (- int(z))
            else: 
                return 0
    
#%%
reverse(-123)

#%% easier version 
def reverse1(x):
    y = list(str(abs(x)))
    y.reverse()
    z= ''.join(x for x in y)
    if x > 0 and int(z) <= (2**31-1):
        return (int(z))
    if x == 0: 
        return 0
    if x < 0 and int(z) <= (2**31-1):
        return (- int(z))
    else: 
        return 0
#%%
reverse1(-123)










