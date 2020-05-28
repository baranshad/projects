# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:29:43 2020

@author: user
"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            ## i is the index num is the value
            ## The problem states you need to return 
            ## indices, so enumerate provides you an index.
            ## By assigning h[num] = i you are creating the first index.
            ## When you identify the compliment you will have the other 
            ## index. when n is in h, i is not in the values of h yet, so h[n] and i are different.
            n = target - num ## num = 2 , n = 9-2= 7
            ## if num = 2, i =0, n = 22-2=20 
            ## it returns a list of 2 elements, 
            ## brackets are lists in python (similar to an array), 
            ## the first element is h[n] which looks up the index of the target 
            if n not in h:
                h[num] = i
            else: ## if n is in h, then h[n] is the index of the compliment element
                return [h[n], i] ## i is the index 
#%%
a = [2, 7, 1, 8, 11, 15]
t = 9
print(twoSum(a,t))  # (1,2)
#%%
a = (-3,4,3,90)
t = 0
print(two_sum(a,t)) 
#%%
def twoSum2(nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []
#%%
print(twoSum2(a,t))
#%%
def twoSum(nums, target):
        a ={}
        for i, num in enumerate(nums):
            if target-num in a:
                return [a[target - num], i]
            else:
                a[num] = i
#%%
def twoSum_lookingindex(nums, target):
        a = {}
        for i, num in enumerate(nums):
            if target-num in a:
                b = [a[target - num], i] ## here i is the index of 2 = 0 
                return b  ## if let the list = [2,7,11,15], t = 9
            ## then a = {2: 0} the index of 2 is 0 
            else:
                a[num] = i
#%%
b = [2, 7, 1, 8, 11, 15]
t = 9
print(twoSum_lookingindex(b,t))
#%%                
## a = {2:0} 
## a[2] = 0 
#%%








