import csv


class ActionOptimized:
    def __init__(self, identifiant, cout, benefice):
        self.identifiant = identifiant
        self.cout = cout
        self.benefice = benefice
        self.ratio = benefice / cout

    def profit(self):
        return self.cout * (self.benefice / 100)

def lire_actions(fichier):
    actions = []
    with open(fichier, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            identifiant = ligne['name']
            cout = float(ligne['price'])
            benefice = float(ligne['profit'])
            # Ignorer les actions avec un coût de 0
            if cout > 0:
                actions.append(ActionOptimized(identifiant, cout, benefice))
    return actions

def trouver_meilleure_combinaison(actions, budget_max=500):
    actions.sort(key=lambda action: action.ratio, reverse=True)
    meilleure_combinaison = []
    budget_actuel = 0
    profit_total = 0
    
    for action in actions:
        if budget_actuel + action.cout <= budget_max:
            meilleure_combinaison.append(action)
            budget_actuel += action.cout
            profit_total += action.profit()

    return meilleure_combinaison, budget_actuel, profit_total

# Exemple d'utilisation
actions = lire_actions('dataset1_Python+P7.csv')
meilleure_combinaison, budget_utilise, profit_total = trouver_meilleure_combinaison(actions)

print("Meilleure combinaison d'actions à acheter :")
for action in meilleure_combinaison:
    print(f"{action.identifiant} (Coût: {action.cout}€, Bénéfice: {action.benefice}%)")
# Afficher la meilleure combinaison et son profit
if meilleure_combinaison:
    total = 0
    print("Meilleure combinaison d'actions à acheter :")
    for action in meilleure_combinaison:
        print(f"{action.identifiant} (Coût: {action.cout}€, Bénéfice: {action.benefice}%)")
        total += action.cout
    total_arrondi = round(total, 2)  # Arrondir le coût total à deux décimales
    print(f"Coût Total : {total_arrondi}€")
    print(f"Profit total : {round(profit_total, 2)}€")  # Arrondir le profit total à deux décimales

