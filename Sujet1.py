# Ex 1

def recherche(caractere, mot) :
    o = 0
    for char in mot :
        if char == caractere : o +=1
    return print(o)
recherche('e', "sciences")
recherche('i',"mississippi")
recherche('a',"mississippi")

# Ex 2
Pieces = [100,50,20,10,5,2,1]
def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:
       return solution
    p = Pieces[i]
    if p <= arendre :
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else :
        return rendu_glouton(arendre, solution, i+1)
print(rendu_glouton(68,[],0))
print(rendu_glouton(291,[],0))