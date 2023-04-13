# Format XML

import xml.dom.minidom as dom

def tailleDOM(d):
    t = 1
    for c in d.childNodes:
        t += tailleDOM(c)
    return t

# Test #

doc1 = dom.parse("fichier.xml")
f = open("fichier.xml")
doc2 = dom.parse(f)
doc3 = dom.parseString("<a>mon joli <b>document</b></a>")

print(tailleDOM(doc3))

doc4 = dom.parseString('<recette difficulté="facile"><titre>Crêpes sucrées</titre><temps>1h</temps><note>pour 10 crêpes</note><ingredients><i q="200g">farine</i><i q="40g">sucre</i><i q="2">oeufs</i><i q="40cl">lait</i></ingredients><etapes><e>mélanger les ingrédients solides</e><e>ajouter le lait</e><e>laisser reposer</e><e>cuire sur une poële beurrée</e></etapes></recette>')

print(tailleDOM(doc4))

doc5 = dom.parseString("<a></a>")

print(" taille d'une arborescence réduite au noeud racine : ",tailleDOM(doc5))
a = doc5.childNodes[0]
b = doc5.createElement("b")
c = doc5.createElement("c")
a.appendChild(b)
a.appendChild(c)

print(" taille après ajout de deux noeud : ",tailleDOM(doc5))

# Format JSON

from json import*

 f = open("recette.json")
 recette = json.load(f)
 f.close()

d = loads('{ "nom" : "Knuth" , "prénom" : "Olaf"}')
print(d["nom"])
print(d["prénom"])

e = loads('{"titre" : "Crêpes sucrées","difficulté" : "facile","temps" : { "unité" : "h", "valeur" : 1 },"note" : "pour 10 crêpes","ingredients" : [{ "nom" : "farine", "q" : { "unité" : "g", "valeur" : 200} },{ "nom" : "sucre", "q" : { "unité" : "g", "valeur" : 200} },{ "nom" : "oeufs", "q" : { "unité" : "", "valeur" : 2} },{ "nom" : "lait", "q" : { "unité" : "cl", "valeur" : 40}}],"étapes" : ["mélanger les ingrédients solides","ajouter le lait","laisser reposer","cuire sur une poële beurrée"]}')
print(e["ingredients"][3]["q"]["valeur"])


d["prénom"] = "Wladimir"
f = open("scandinavie.json", "w+")
dump(d, f)
f.close()

f2 = open("scandinavie.json")
repertoire = load(f2)
f2.close()
print("le fichier scandinavie.json contient maintenant : ",repertoire["nom"]," , ",repertoire["prénom"])
print('-------------------------------------------------------')

h = { 'début' : 'EXEMPLE' , 'suite' : { 'a' : None, 'b' : False} , 'fin' : 421, "test": 4.4564544465446546545489454655e20}
print(" le dictionnaire Python h est traduit en :")
print(dumps(h))

for n in e.keys():
    if n=="ingredients":
        for k in range(4):
            e[n][k]["q"]["valeur"] *= 2
f = open("recette.json", "w+")
dump(e, f)
f.close()

f = open("recette.json")
recette = load(f)
f.close()
print(dumps(recette))