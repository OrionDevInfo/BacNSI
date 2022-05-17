# Ex 1
def calcul(n) :
    un = []
    while n != 1 :
        un.append(int(n))
        if n % 2 == 0 : n /= 2
        else : n = 3*n + 1
    un.append(1)
    return print(un)
calcul(7)

# Ex 2
dico = {
    "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7,
    "H":8, "I":9, "J":10, "K":11, "L":12, "M":13,
    "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19,
    "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26
}
def est_parfait(mot) :
    #mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""
    code_a = 0
    for c in mot :
      code_c = code_c + f'{dico[c]}'
      code_a += dico[c]
    code_c = int(code_c)
    if code_c % code_a == 0 :
      mot_est_parfait = True
    else :
      mot_est_parfait = False
    return print([code_a, code_c, mot_est_parfait])
est_parfait("PAUL")
est_parfait("ALAIN")