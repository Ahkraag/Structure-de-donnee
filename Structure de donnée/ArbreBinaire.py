class Noeud:

    def __init__(self, v, g, d):
        assert g is None or type(g) == Noeud, "Le type de g ne sont pas bon"
        assert d is None or type(d) == Noeud, "Le type de d ne sont pas bon"
        self.valeur = v
        self.gauche = g
        self.droit = d

# Test #

a = Noeud("A", Noeud("B", None, Noeud("C", None, None)), Noeud("D", None, None))
a.gauche.gauche=Noeud("E",Noeud("G", None, None),Noeud("H", None, Noeud("K", None, None)))
a.droit.droit=Noeud("N", Noeud("T", None, None), None)
a.droit.gauche=Noeud("L", Noeud("M", None, None), None)

##########

def taille2(abr):
    if abr is None:
        return 0
    return 1 + taille2(abr.gauche) + taille2(abr.droit)


def hauteur2(abr):
    if abr is None:
        return 0
    return 1 + max(hauteur2(abr.gauche), hauteur2(abr.droit))

# Test #
print(taille2(a))
print(hauteur2(a))

#### Parcours

def infixe(abr):
    if abr is None:
        pass
    else:
        infixe(abr.gauche)
        print(abr.valeur, end=', ')
        infixe(abr.droit)

def prefixe(abr):
    if abr is None:
        pass
    else:
        print(abr.valeur, end=', ')
        prefixe(abr.gauche)
        prefixe(abr.droit)

def postfixe(abr):
    if abr is None:
        pass
    else:
        postfixe(abr.gauche)
        postfixe(abr.droit)
        print(abr.valeur, end=', ')

def parcours(abr):
    h = hauteur2(abr)
    for i in range(1, h):
        étage(abr, i)

def étage(abr, i):
    if abr is None:
        return
    if i == 1:
        print(abr.valeur, end=", ")
    elif i > 1:
        étage(abr.gauche, i-1)
        étage(abr.droit, i-1)


##### Class avec les fonctions

class ArbreBinaire:

    def __init__(self, v=None, g=None, d=None):
        assert g is None or type(g) == ArbreBinaire, "Le type de g ne sont pas bon"
        assert d is None or type(d) == ArbreBinaire, "Le type de d ne sont pas bon"
        self.valeur = v
        self.gauche = g
        self.droit = d

    def taille(self):
        if self.valeur is None:
            return 0
        return 1 + self.gauche.taille() + self.droit.taille()

    def hauteur(self):
        if self.valeur is None:
            return 0
        return 1 + max(self.gauche.hauteur(), self.droit.hauteur())

    def prefixe(self):
        if self.valeur is None:
            pass
        else:
            print(self.valeur, end=', ')
            self.gauche.prefixe()
            self.droit.prefixe()

    def postfixe(self):
        if self.valeur is None:
            pass
        else:
            self.gauche.postfixe()
            self.droit.postfixe()
            print(self.valeur, end=', ')

    def infixe(self):
        if self.valeur is None:
            pass
        else:
            self.gauche.infixe()
            print(self.valeur, end=', ')
            self.droit.infixe()

    def parcours(self):
        h = self.hauteur()
        for i in range(1, h):
            self.étage(i)

    def étage(self, i):
        if self.valeur is None:
            return
        if i == 1:
            print(self.valeur, end=", ")
        elif i > 1:
            self.gauche.étage(i - 1)
            self.droit.étage(i - 1)

    def affiche(self):
        if self.valeur is None:
            print("⊥", end="")
        else:
            print("(", end="")
            self.gauche.affiche()
            print(", " + self.valeur, end=", ")
            self.droit.affiche()
            print(")", end="")

##########

def parfait(h):
    if h == 0:
        return ArbreBinaire()
    return ArbreBinaire("Arbre", parfait(h - 1), parfait(h - 1))

# Test #

v = ArbreBinaire()
b = ArbreBinaire("A", ArbreBinaire("B", v, ArbreBinaire("C", v, v)), ArbreBinaire("D", v, v))
b.gauche.gauche=ArbreBinaire("E",ArbreBinaire("G", v, v),ArbreBinaire("H", v, ArbreBinaire("K", v, v)))
b.droit.droit=ArbreBinaire("N", ArbreBinaire("T", v, v), v)
b.droit.gauche=ArbreBinaire("L", ArbreBinaire("M", v, v), v)

print(b.taille())
print(b.hauteur())
b.prefixe()
print()
b.postfixe()
print()
b.infixe()
print()
b.parcours()
print()
b.affiche()
print()
parfait(10).affiche()
