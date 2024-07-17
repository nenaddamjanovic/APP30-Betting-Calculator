def calculate_weighted_score(odds, last_five_games):
    # Ponderisanje rezultata utakmica, gde je najnovija utakmica najvažnija
    weights = [5, 4, 3, 2, 1]
    score = sum([weights[i] * (1 if result == 'W' else 0.50 if result == 'D' else -0.10) for i, result in
                 enumerate(last_five_games)])
    # Uzimamo u obzir i kvotu, gde manja kvota dobija veći skor
    print(f"koeficijent na osnovu zadnjih 5 utakmica je {score}")
    weighted_score = score / odds
    print(f"ukupni koeficijent na osnovu utakmica/kvota je {weighted_score}")
    return weighted_score