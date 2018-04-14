#!/usr/bin/env python

def removeStr(input):
    result = []
    for c in input:
        if c not in result:
            result.append(c)
    result = ''.join(result)
    print result

input = "this is a string"
removeStr(input)
