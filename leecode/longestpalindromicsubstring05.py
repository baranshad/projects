# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:17:17 2020

@author: user
"""


## 5 longest palindromic substriing 
## Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000. 
###  Palindromic prime numbers are those which read the same backwards as forwards.

#%% 
def longestPalindrome(s: str):
   tlen=[]
   tlist=[]
   for i in range(len(s)):
      for j in range(i+1, len(s)):
         t = s[i:j+1]
         if t == t[::-1]: 
            tlist.append(t)
            tlen.append(len(t))     
         else: 
            None
   d = dict(zip(tlist, tlen))
   return(max(d, key=d.get)) 
#%%
longestPalindrome("malayalam")

#%%
def isPalindrome(s): 
    return s == s[::-1] 

s = "malayalam"
ans = isPalindrome(s) 
  
if ans: 
    print("Yes") 
else: 
    print("No")
#%% approach from others
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''  # Memory to remember a palindrome
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s), i, -1):  # j = end, O = n^2
                if len(m) >= j-i:  # To reduce time
                    break
                elif s[i:j] == s[i:j][::-1]:
                    m = s[i:j]
                    break
        return m
#%%














