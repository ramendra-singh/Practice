#!/usr/bin/env python

def nonRepeatStr(input):
    result = []
    k = 0
    count = [0] * 256
    for i in input:
        count[ord(i)]+=1

    for i in input:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1

    print input[index]



input = "geeksforgeeks"
nonRepeatStr(input)
