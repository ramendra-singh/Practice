def stringRotation(string1, string2):
    temp = string1 + string1

    if (temp.count(string2) > 0):
        return True
    else:
        return False

string1 = "AACD"
string2 = "ACDA"

if stringRotation(string1, string2):
    print "Strings are rotations of each other"
else:
    print "Strings are not rotations of each other"
