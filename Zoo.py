from abc import ABC, abstractmethod
import json


class Animal(ABC):
    def __init__(self, code, nom_scientifique, espece, nombre_de_pieds, pays_origine):
        self.code = code
        self.nom_scientifique = nom_scientifique
        self.espece = espece
        self.nombre_de_pieds = nombre_de_pieds
        self.pays_origine = pays_origine

    def afficher_info(self):
        print(f"Code : {self.code}")
        print(f"Nom scientifique : {self.nom_scientifique}")
        print(f"Espèce : {self.espece}")
        print(f"Nombre de pieds : {self.nombre_de_pieds}")
        print(f"Pays d'origine : {self.pays_origine}")

    @abstractmethod
    def se_deplacer(self):
        pass

# Sous-classes d'Animal
class Chien(Animal):
    def se_deplacer(self):
        print("Le chien se déplace sur 4 pieds.")

    def afficher_info(self):
        super().afficher_info()
        print("C'est un Chien.")
class Chat(Animal):
    def se_deplacer(self):
        print("Le chat se déplace sur 4 pieds.")
    def afficher_info(self):
        super().afficher_info()
        print("C'est un Chat.")
class Poulet(Animal):
    def se_deplacer(self):
        print("Le poulet se déplace sur 2 pattes.")
    def afficher_info(self):
        super().afficher_info()
        print("C'est un Poulet.")
class Vache(Animal):
    def se_deplacer(self):
        print("La vache se déplace sur 4 pieds.")
    def afficher_info(self):
        super().afficher_info()
        print("C'est une Vache.")
class Zoo:
    def __init__(self, nom, superficie):
        self.nom = nom
        self.superficie = superficie
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)
#other code
    def supprimer_animal(self, code):
        self.animaux = [animal for animal in self.animaux if animal.code != code]

    def update_animal(self, nom_animal, **modifications):
        for animal in self.animaux:
            if animal.nom_scientifique == nom_animal:
                for key, value in modifications.items():
                    setattr(animal, key, value)
                print(f"Les informations de l'animal {nom_animal} ont été mises à jour.")
                return
        print(f"Aucun animal avec le nom scientifique {nom_animal} n'a été trouvé.")

    def chercher_animal(self, espece):
        for animal in self.animaux:
            if animal.espece.lower() == espece.lower():
                animal.afficher_info()
#char7
    def tri_animaux(self):
        self.animaux.sort(key=lambda x: x.nom_scientifique)
        print("Les animaux ont été triés par nom scientifique.")

    def afficher_animaux(self):
        if self.animaux:
            for animal in self.animaux:
                animal.afficher_info()
                print(f"L'animal appartient au zoo {self.nom}.")
        else:
            print("Aucun animal dans le zoo.")

    def Enregistrer_Animal(self, fichier="animal.txt"):
        with open(fichier, "w", encoding="utf-8") as file:
            file.write(f"Zoo : {self.nom}, Superficie : {self.superficie}\n")
            file.write("Liste des animaux :\n")
            for animal in self.animaux:
                file.write(
                    f"{animal.code}, {animal.nom_scientifique}, {animal.espece}, "
                    f"{animal.nombre_de_pieds}, {animal.pays_origine}\n"
                )
        print(f"Les animaux ont été enregistrés dans le fichier {fichier}.")

    def Load_JSON(self, fichier="Animal.json"):
        try:
            with open(fichier, "r", encoding="utf-8") as file:
                animaux_data = json.load(file)
                for data in animaux_data:
                    if 'espece' not in data:
                        print(f"Clé 'espece' manquante dans l'enregistrement : {data}")
                        continue

                    espece = data['espece'].lower()
                    if espece == "chien":
                        animal = Chien(
                            data['code'], data['nom_scientifique'], data['espece'],
                            data['nombre_de_pieds'], data['pays_origine']
                        )
                    elif espece == "chat":
                        animal = Chat(
                            data['code'], data['nom_scientifique'], data['espece'],
                            data['nombre_de_pieds'], data['pays_origine']
                        )
                    elif espece == "poulet":
                        animal = Poulet(
                            data['code'], data['nom_scientifique'], data['espece'],
                            data['nombre_de_pieds'], data['pays_origine']
                        )
                    elif espece == "vache":
                        animal = Vache(
                            data['code'], data['nom_scientifique'], data['espece'],
                            data['nombre_de_pieds'], data['pays_origine']
                        )
                    else:
                        print(f"Espèce inconnue : {data['espece']}. Ignorée.")
                        continue
                    self.ajouter_animal(animal)
            print(f"Les animaux ont été chargés depuis le fichier {fichier}.")
        except FileNotFoundError:
            print(f"Le fichier {fichier} n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur dans le format du fichier JSON.")

# Code principal
zoo = Zoo("Zoo National", 5000)

# Ajout d'animaux
chien = Chien("001", "Canis lupus familiaris", "chien", 4, "France")
chat = Chat("002", "Felis catus", "chat", 4, "Egypte")
poulet = Poulet("003", "Gallus gallus domesticus", "poulet", 2, "Inde")
vache = Vache("004", "Bos taurus", "vache", 4, "Inde")

zoo.ajouter_animal(chien)
zoo.ajouter_animal(chat)
zoo.ajouter_animal(poulet)
zoo.ajouter_animal(vache)

# Affichage des animaux
print("\nAnimaux dans le zoo :")
zoo.afficher_animaux()

# Enregistrement dans un fichier texte
zoo.Enregistrer_Animal()

# Chargement des animaux depuis un fichier JSON
zoo.Load_JSON("Animal.json")
