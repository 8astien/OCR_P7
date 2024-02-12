import csv

class ActionOptimized:
    def __init__(self, identifiant, cout, benefice):
        self.identifiant = identifiant
        self.cout = cout
        self.benefice = benefice

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
            if cout > 0:
                actions.append((identifiant, cout, cout * benefice / 100))
    return actions

def trouver_meilleure_combinaison(actions, budget_max):
    n = len(actions)
    dp = [[0 for x in range(int(budget_max) + 1)] for x in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, int(budget_max) + 1):
            cout, profit = actions[i-1][1], actions[i-1][2]
            if cout <= w:
                dp[i][w] = max(profit + dp[i-1][int(w-cout)], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = budget_max
    selected_actions = []
    cost_total = 0
    for i in range(n, 0, -1):
        if dp[i][int(w)] != dp[i-1][int(w)] and actions[i-1][1] + cost_total <= budget_max:
            selected_actions.append(actions[i-1])
            w -= actions[i-1][1]
            cost_total += actions[i-1][1]

    selected_actions.reverse()
    profit_total = dp[n][int(budget_max)]
    return profit_total, selected_actions, cost_total


fichier_csv = 'dataset2_Python+P7.csv'
actions = lire_actions(fichier_csv)
profit_total, actions_selectionnees, cout_total = trouver_meilleure_combinaison(actions, 500)

print("Meilleure combinaison d'actions à acheter :")
for identifiant, cout, profit in actions_selectionnees:
    print(f"{identifiant} (Coût: {cout}€, Bénéfice: {profit/cout*100}%)")
print(f"Coût Total : {cout_total}€")
print(f"Profit total : {profit_total}€")
