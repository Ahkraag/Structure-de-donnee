# autre type de structures de donnée : Arborescence, des arbres avec plusieurs fils

class Noeud:

    def __init__(self, r="A", fils={}):
        self.valeur = r
        self.fils = fils


def taille(abr):
    t = 1
    for e in abr.fils:
        t += taille(e)
    return t


def affiche(abr):
    t = str(abr.valeur) + " | "
    for e in abr.fils:
        t += affiche(e)
    return t


def hauteur(abr):
    h = 1
    t = [0] * len(abr.fils)
    for k in range(len(t)):
        t[k] = hauteur(abr.fils[k])
    if len(t) != 0: h += max(t)
    return h


def maximum(abr):
    t = abr.valeur
    for e in abr.fils:
        m = maximum(e)
        if m > t:
            t = m
    return t

# Test #

m=Noeud("C",{})
x=Noeud("A",{Noeud("B",{Noeud("D",{})}),Noeud("C",{Noeud("E",{}),Noeud("F",{Noeud("H",{})}),Noeud("G",{})})})
j=Noeud("A",[Noeud("B",[Noeud("D",[])]),Noeud("C",[Noeud("E",[]),Noeud("F",[Noeud("H",[])]),Noeud("G",[])])])
m=Noeud(1,[Noeud(4,[Noeud(9,[])]),Noeud(12,[Noeud(11,[]),Noeud(10,[Noeud(95,[])]),Noeud(22,[])])])
print(f"La taille de cet arborescence est : {taille(x)}")
print(f"Le parcours préfixe de cette arborescence est : {affiche(j)}")
print(f"La hauteur de cette arborescence est : {hauteur(j)}")
print(f"Le maximum de cette arborescence est : {maximum(m)}")