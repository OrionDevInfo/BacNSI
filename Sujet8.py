# Ex 1
def recherche(elt, tab) :
    i = -1
    for j in range(0, len(tab)) :
        if tab[j] == elt : i = j
    return print(i)
recherche(1, [2, 3, 4])
recherche(1, [10, 12, 1, 56])
recherche(50, [1, 50, 1])
recherche(15, [8, 9, 10, 15])

# Ex 2
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l)-2
    while a < l[i] and i >= 0:
      l[i+1] = l[i]
      l[i] = a
      i = i-1
    return print(l)
insere(3,[1,2,4,5])
insere(10,[1,2,7,12,14,25])
insere(1,[2,3,4])