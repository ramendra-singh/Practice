def permutation(a,l,r):
    if l==r:
        print ''.join(a)
    else:
        for i in range(l,r+1):
            a[l],a[i]=a[i],a[l]
            permutation(a,l+1,r)
            a[l],a[i]=a[i],a[l]

string1 = 'abcd'
n = len(string1)
a = list(string1)
permutation(a,0,n-1)
