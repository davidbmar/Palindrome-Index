#!/bin/python

import sys

def reverseString(myString):
    return myString[::-1]

def isPalindrome(aString):
    #reverse the string
    reversedStr=""
    reversedStr=reverseString(aString)
    if (reversedStr == aString):
        #print ("{} it is a palindrome of {}".format(reversedStr,aString))
        return 1
    else:
        #print ("{} is not a palindrome of {}".format(reversedStr,aString))
        return 0
    
# This function will basically remove a given index 
def stringWithoutIndex(s,myRemovalIndex):
    return s[:myRemovalIndex]+s[myRemovalIndex+1:]

def palindromeIndex(s):
    # Complete this function
    # first determine if it is a palindrome now without removal of any letter.
    strLenPalindrome=len(s)
    
    i=int()
    if(isPalindrome(s)==1):
        return -1
    else:
        myReverseString=reverseString(s)
        for i in range(strLenPalindrome/2):
            # march from ends of line for both the string and the reversed string.
            if (s[i]==myReverseString[i]):
                pass
            else:
                # try removing i in both the normal string and the reversed string
                aCompareStrMissingIndex=stringWithoutIndex(s,i)
                aReverseCompareStrMissingIndex=stringWithoutIndex(myReverseString,i)
                if(isPalindrome(aCompareStrMissingIndex)==1):
                    return i
                elif(isPalindrome(aReverseCompareStrMissingIndex)==1):
                    return strLenPalindrome-i-1
        return -1

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = palindromeIndex(s)
    print(result)
