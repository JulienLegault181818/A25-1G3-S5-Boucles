def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température (°C)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : humidité (%)

    Retour :
    - "Tout est sous contrôle!" si tout est bon
    - "Environnement non optimal" avec les problèmes sinon
    """
    problemes = []

    # Vérification de la température (optimal entre 20 et 25°C)
    if not (20 <= temp <= 25):
        problemes.append("Température non optimale (idéalement entre 20 et 25°C)")

    # Vérification de la poussière
    if poussiere != "faible":
        problemes.append(f"Niveau de poussière non optimal (actuel : {poussiere}, idéal : faible)")

    # Vérification de l'humidité (optimal entre 30 et 60%)
    if not (30 <= humidite <= 60):
        problemes.append("Humidité non optimale (idéalement entre 30 et 60%)")

    if not problemes:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal. Problèmes : " + "; ".join(problemes)


if __name__ == "__main__":
    print(environnement_optimal(25, "faible", 40))  # Tout est sous contrôle!
    print(environnement_optimal(30, "faible",
                                40))  # Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C)
    print(environnement_optimal(25, "faible",
                                20))  # Environnement non optimal. Problèmes : Humidité non optimale (idéalement entre 30 et 60%)
    print(environnement_optimal(30, "moyen",
                                25))  # Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C); Niveau de poussière non optimal (actuel : moyen, idéal : faible); Humidité non optimale (idéalement entre 30 et 60%)
    print(environnement_optimal(18, "faible",
                                45))  # Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C)

    """
    # Plan de tests pour `environnement_optimal`
########################################################################################################################
| Température (°C) | Poussière   | Humidité (%) | Comportement attendu                                                                                                  | Résultat attendu                                                                                                                                                                                                                                                                      |
| 25               | faible      | 40           | Toutes les conditions sont optimales.                                                                                 | Tout est sous contrôle!                                                                                                                                                                                                                                                               |
| 30               | faible      | 40           | Température trop élevée (hors de la plage 20-25°C).                                                                   | Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C)                                                                                                                                                                                       |
| 25               | faible      | 20           | Humidité trop basse (hors de la plage 30-60%).                                                                        | Environnement non optimal. Problèmes : Humidité non optimale (idéalement entre 30 et 60%)                                                                                                                                                                                           |
| 30               | moyen       | 25           | Température trop élevée, poussière non faible, humidité trop basse.                                                   | Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C); Niveau de poussière non optimal (actuel : moyen, idéal : faible); Humidité non optimale (idéalement entre 30 et 60%)                                                               |
| 18               | faible      | 45           | Température trop basse (hors de la plage 20-25°C).                                                                    | Environnement non optimal. Problèmes : Température non optimale (idéalement entre 20 et 25°C)                                                                                                                                                                                       |


########################################################################################################################


    """
