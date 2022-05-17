# Ex 1
def moyenne(l) :
    s, coeff = 0, 0
    for couple in l :
        s += couple[0] * couple[1]
        coeff += couple[1]
    return s / coeff
print(moyenne([(15,2),(9,1),(12,3)]))

# Ex 2
def pascal(n):
    C= [[1]]
    for k in range(1,n+1):
        Ck = [1]
        for i in range(1,k):
            Ck.append(C[k-1][i-1]+C[k-1][i] )
        Ck.append(1)
        C.append(Ck)
    return C
print(pascal(4))
print(pascal(5))