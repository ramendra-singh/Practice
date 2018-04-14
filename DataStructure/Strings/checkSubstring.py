def checkSubstr(string1, string2):
    if (string1.count(string2) > 0):
        return True
    else:
        return False

string1 = "AACD"
string2 = "AC"

if checkSubstr(string1, string2):
    print "Substring -> True"
else:
    print "Substring -> False"
