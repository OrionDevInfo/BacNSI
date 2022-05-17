# Ex 1
def maxi(tab) :
    max = (0,0)
    for i in range(0, len(tab)-1):
        if tab[i] > max[0] : max = (tab[i], i)
    return print(max)
maxi([1,5,6,9,1,2,3,7,9,8])

# Ex 2
def recherche(gene, seq_adn):
    n = len(seq_adn)
    g = len(gene)
    i = 0
    trouve = False
    while i < n and trouve == False :
        j=0
        while j < g and gene[j] == seq_adn[i+j]:
            j+=1
        if j == g:
            trouve = True
        i+=1
    return print(trouve)

recherche("AATC", "GTACAAATCTTGCC")
recherche("AGTC", "GTACAAATCTTGCC")