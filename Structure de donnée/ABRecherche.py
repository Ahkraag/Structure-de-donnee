#Manipulation du module binarytree

from binarytree import*

a=Node('A')
b=Node('B')
c=Node('C')
e=Node(8,Node(2,Node(1),Node(3)),Node(41, Node(52, Node(12))))
ee=Node(8,Node(2, Node(1),Node(3)),Node(52, Node(41, Node(12))))
graph=e.graphviz()
graph

# class

class Noeud:
    def __init__(self, valeur, gauche=None, droit=None):
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit

    def __eq__(self, abr):
        if self is None:
            return abr is None
        elif abr is None:
            return False
        else:
            return ((self.gauche == abr.gauche) and (self.valeur == abr.valeur) and (self.droit == abr.droit))

# Fonction sur l'arbre

def parfait(h):
    if h == 0:
        return None
    else:
        gauche = parfait(h - 1)
        droit = parfait(h - 1)
        racine = Noeud(h, gauche, droit)
        h = h - 1
        return racine


def peigne_gauche(h):
    if h == 0:
        return None
    else:
        gauche = peigne_gauche(h - 1)
        droit = None
        racine = Noeud(h, gauche, droit)
        h = h - 1
        return racine


def traducteur(abr):
    if abr is None:
        return
    else:
        return Node(abr.valeur, traducteur(abr.gauche), traducteur(abr.droit))

def appartient(x,abr):
    if abr is None:
        return False
    elif abr.valeur==x:
        return True
    elif x>abr.valeur:
        return appartient(x,abr.droit)
    else:
        return appartient(x,abr.gauche)


def ajout(x,abr):
    if abr is None:
        return Noeud(x,None,None)
    if x>abr.valeur:
        return Noeud(abr.valeur,abr.gauche,ajout(x,abr.droit))
    else:
        return Noeud(abr.valeur,ajout(x,abr.gauche),abr.droit)

#Sans les doublons
def ajout_V1(x, abr):
    if abr is None:
        return Noeud(x, None, None)
    if x == abr.valeur:
        return abr
    elif x > abr.valeur:
        return Noeud(abr.valeur, abr.gauche, ajout_V1(x, abr.droit))
    else:
        return Noeud(abr.valeur, ajout_V1(x, abr.gauche), abr.droit)


def maximum(abr):
    if abr is None:
        return
    if abr.droit is None:
        return abr.valeur
    return maximum(abr.droit)


def supprime_maximum(abr):
    assert abr is not None, "l'arbre est vide !!!!!!!!! *#@!/%"
    if abr.droit is None:
        return abr.gauche
    return Noeud(abr.valeur, abr.gauche, supprime_maximum(abr.droit))


def suppression(x, abr):
    if abr is None:
        return None
    if x < abr.valeur:
        return Noeud(abr.valeur, suppression(x, abr.gauche), abr.droit)
    if x > abr.valeur:
        return Noeud(abr.valeur, abr.gauche, suppression(x, abr.droit))
    if abr.gauche is None:
        return abr.droit
    return Noeud(maximum(abr.gauche), supprime_maximum(abr.gauche), abr.droit)



# Test #

ex1 = Noeud(3, Noeud(1, None, Noeud(2, None, None)), Noeud(4, None, None))
ex11= traducteur(ex1).graphviz()
ex11
ex22= None

ex3 = ajout_V1(0, ex1)
ex3 = ajout_V1(5, ex3)
ex3 = ajout_V1(5, ex3)
print(ex3.valeur)
traducteur(ex3)

m=appartient(5,ex1)
j=appartient(4,ex1)
p=appartient(1,ex1)
print("la valeur 5 est-elle dans l'arbre ? ",m)
print("la valeur 4 est-elle dans l'arbre ? ",j)
print("la valeur 1 est-elle dans l'arbre ? ",p)