# Ex 1
def conv_bin(n) :
    b, binary = [], bin(n)[2:]
    for i in binary: b.append(i)
    bit = len(b)
    return (b, bit)
print(conv_bin(9))

# Ex 2
def tri_bulles(T):
    n = len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            print(T, i, j)
            if T[j] > T[j+1]:
                temp = T[j]
                T[j] = T[j+1]
                T[j+1] = temp
    return T
print(tri_bulles([1,5,6,9,1,2,3,7,9,8]))