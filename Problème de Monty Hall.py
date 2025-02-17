import random

def scenario_genie():
    # Initialiser les portes
    portes = [0, 0, 0]  # 0 représente une porte sans trésor

    # Placer le trésor derrière l'une des portes au hasard
    porte_tresor = random.randint(0, 2)
    portes[porte_tresor] = 1  # 1 représente une porte avec le trésor

    # Aladin choisit une porte au hasard
    choix_initial = random.randint(0, 2)

    # Le Génie ouvre l'une des deux portes restantes ne cachant pas le trésor
    portes_restantes = [i for i in range(3) if i != choix_initial and portes[i] == 0]
    porte_ouverte = random.choice(portes_restantes)

    # Aladin peut maintenant changer de porte ou rester avec son choix initial
    # Changer de porte
    choix_final = [i for i in range(3) if i != choix_initial and i != porte_ouverte][0]

    # Renvoie True si Aladin a trouvé le trésor en validant son choix initial, False sinon
    # Renvoie True si Aladin a trouvé le trésor en changeant son choix initial, False sinon
    return portes[choix_initial] == 1, portes[choix_final] == 1

# Nombre de simulations
nombre_simulations = 100000

# Compteur de réussites en validant le choix initial
reussites_initial = 0

# Compteur de réussites en changeant le choix initial
reussites_changement = 0

# Exécuter les simulations
for _ in range(nombre_simulations):
    resultat_initial, resultat_changement = scenario_genie()
    reussites_initial += resultat_initial
    reussites_changement += resultat_changement

# Afficher les résultats
print(f"Réussites en validant le choix initial : {reussites_initial}")
print(f"Réussites en changeant le choix initial : {reussites_changement}")
