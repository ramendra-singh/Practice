'''
Program to Check if a Given String is Palindrome
Given a string, write a c function to check if it is palindrome or not.
A string is said to be palindrome
if reverse of the string is same as string. For example,
"abba" is palindrome, but "abbc" is not palindrome.
'''


def pallindrome(input):
    length = len(input)
    list1 = list(input)
    for i in range(length):
        if list1[i] != list1[length-1-i]:
            return 0

    print "String is pallindorme -> %s" % input

pallindrome('ABCDCBA')
pallindrome('ABCDC')
pallindrome('ABCDCB')
