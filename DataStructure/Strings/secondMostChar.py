'''
Program to find second most frequent character
Given a string, find the second most frequent character in it. Expected time complexity is O(n) where n is the length of the input string.

Examples:

Input: str = "aabababa";
Output: Second most frequent character is 'b'

Input: str = "geeksforgeeks";
Output: Second most frequent character is 'g'

Input: str = "geeksquiz";
Output: Second most frequent character is 'g'
The output can also be any other character with
count 1 like 'z', 'i'.

Input: str = "abcd";
Output: No Second most frequent character
A simple solution is to start from the first character, count its occurrences, then second character and so on. While counting these occurrence keep track of max and second max. Time complexity of this solution is O(n2).
We can solve this problem in O(n) time using a count array with size equal to 256 (Assuming characters are stored in ASCII format).
'''

def secondMostChar(input):
    count = [0] * 256
    for i in input:
        count[ord(i)] += 1

    max = -1
    first = 0
    second = 0
    for i in range(256):
        if count[i] > count[first]:
            second = first
            first = i
        elif count[i] > count[second] and count[i] != count[first]:
            second = i

    for i in input:
        if count[ord(i)] == count[second]:
            print i
            break

input = "aabababa"
secondMostChar(input)
