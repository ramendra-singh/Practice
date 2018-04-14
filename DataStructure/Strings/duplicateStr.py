#!/usr/bin/env python

def duplicateStr(input):
    d = {}
    for c in input:
        try:
            d[c] += 1
        except:
            d[c] = 1

    for k in d.keys():
        print "%s: %d" % (k, d[k])

input = "this is a string"
duplicateStr(input)
