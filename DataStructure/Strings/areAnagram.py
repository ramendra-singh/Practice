'''
Check whether two strings are anagram of each other
Write a function to check whether two given strings are anagram of each other
or not. An anagram of a string is another string that contains same characters,
only the order of characters can be different.
For example, "abcd" and "dabc" are anagram of each other.c
heck-whether-two-strings-are-anagram-of-each-other
'''

def areAnagram(input1,input2):
    count1 = [0] * 256
    count2 = [0] * 256

    for i in input1:
        count1[ord(i)] += 1

    for i in input2:
        count2[ord(i)] += 1

    for i in xrange(256):
        if count1[i] != count2[i]:
            return 0

    return 1

# Driver program to test the above functions
input1 = "listen"
input2 = "silent"
if areAnagram(input1, input2):
    print "The two strings are anagram of each other"
else:
    print "The two strings are not anagram of each other"
