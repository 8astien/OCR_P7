import csv
from itertools import combinations

# Représente les actions, avec méthode profit pour calculer le profit potentiel par action
class Action:
    def __init__(self, identifiant, cout, benefice):
        self.identifiant = identifiant
        self.cout = float(cout)
        self.benefice = float(benefice)

    def profit(self):
        return self.cout * (self.benefice / 100)

def read_csv(fichier_csv):
    actions = []
    with open(fichier_csv, mode='r', encoding='utf-8') as fichier:
        reader = csv.reader(fichier)
        next(reader)  # Sauter l'en-tête
        for line in reader:
            if line:  # S'assurer que la ligne n'est pas vide
                identifiant, cout, benefice = line
                actions.append(Action(identifiant, cout, benefice))
    return actions

# Remplacer le chemin par le chemin réel de votre fichier CSV
csv_file = 'premier_dataset.csv'
# csv_file = 'dataset2_Python+P7.csv'
# csv_file = 'premier_dataset.csv'
actions = read_csv(csv_file)

#Fonction pour calculer le coût total et le profit total d'une combinaison d'actions
def evaluer_combinaison(combinaison):
    cout_total = sum(action.cout for action in combinaison)
    profit_total = sum(action.profit() for action in combinaison)
    return cout_total, profit_total

# Trouver la meilleure combinaison
meilleure_combinaison = None
meilleur_profit = 0

# Générer toutes les combinaisons possibles et évaluer chacune
# utilisation de combinations de itertools pour simplifier les combinaisons d'associaitions
for i in range(1, len(actions) + 1):
    for combinaison in combinations(actions, i):
        cout_total, profit_total = evaluer_combinaison(combinaison)
        if cout_total <= 500 and profit_total > meilleur_profit:
            meilleure_combinaison = combinaison
            meilleur_profit = profit_total

# Afficher la meilleure combinaison et son profit
if meilleure_combinaison:
    total = 0
    print("Meilleure combinaison d'actions à acheter :")
    for action in meilleure_combinaison:
        print(f"{action.identifiant} (Coût: {action.cout}€, Bénéfice: {action.benefice}%)")
        total += action.cout
    print(f"Coût Total : {total}")
    print(f"Profit total : {meilleur_profit}€")
else:
    print("Aucune combinaison trouvée respectant le budget de 500€")