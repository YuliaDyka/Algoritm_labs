def prefix(s):
    P = [0]*len(s)
    j = 0
    i = 1
    
    while i < len(s):
        if s[j] != s[i]:
            if j > 0:
                j = P[j-1]
            else:           # j == 0
                i += 1
        else:               # s[j] == s[i]
            P[i] = j + 1
            i += 1
            j += 1

    return P

def kmp(sub:str, s:str):
    """Search substring in string Knuth, Morris, Prath
    Arguments:
        sub {str} -- substring
        s {str} -- string
    """
    k = 0
    l = 0
    P = prefix(sub)

    while k < len(s):
        if sub[l] == s[k]:
            k += 1
            l += 1

            if l == len(sub):
                return k - len(sub)

        elif l > 0:
            l = P[l-1]
        else:
            k += 1

    return -1