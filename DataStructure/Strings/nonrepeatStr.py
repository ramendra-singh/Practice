#!/usr/bin/env python

def printList(items,str1):

    for _item in items:
        found = True
        for _t in str1:
            if _item.count(_t) > 0:
                continue
            else:
                found = False
                break
        if found:
            print _item

str1 = "sun"
items = ["geeksforgeeks", "unsorted", "sunday", "just", "sss"]
printList(items,str1)
