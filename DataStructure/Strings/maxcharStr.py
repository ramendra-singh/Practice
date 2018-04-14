#!/usr/bin/env python

def maxRepeatStr(input):
    result = []
    k = 0
    count = [0] * 256
    for i in input:
        count[ord(i)]+=1

    max = -1
    for i in input:
        if max < count[ord(i)]:
            c = i
            max = count[ord(i)]

    print c

input = "geeksforgeeks"
maxRepeatStr(input)

'''
Input string = 'test'
1: Construct character count array from the input string.
  count['e'] = 1
  count['s'] = 1
  count['t'] = 2

2: Return the index of maximum value in count array (returns 't')
'''
