
def calculate_weighted_score(odds, last_five_games):
    # Ponderisanje rezultata utakmica, gde je najnovija utakmica najvažnija
    weights = [5, 4, 3, 2, 1]
    score = sum([weights[i] * (0.40 if result == 'W' else 0.25 if result == 'D' else 0) for i, result in enumerate(last_five_games)])
    # Uzimamo u obzir i kvotu, gde manja kvota dobija veći skor
    weighted_score = score / odds
    print(score)
    return weighted_score

def main():
    print("Unesite kvote za opcije 1, X i 2:")

    # Dodavanje koeficijenta za domaćina
    home_advantage = 0.15

    # Unos kvota
    odds_1 = float(input("Kvote za 1: "))
    odds_X = float(input("Kvote za X: "))
    odds_2 = float(input("Kvote za 2: "))

    print("Unesite rezultate poslednjih 5 utakmica za tim 1 (W, D ili L):")
    last_five_team1 = [input(f"Rezultat utakmice {i+1} za tim 1: ").upper() for i in range(5)]

    print("Unesite rezultate poslednjih 5 utakmica za tim 2 (W, D ili L):")
    last_five_team2 = [input(f"Rezultat utakmice {i+1} za tim 2: ").upper() for i in range(5)]

    # Izračunavanje ponderisanih skorova
    score_1 = calculate_weighted_score(odds_1, last_five_team1)
    score_2 = calculate_weighted_score(odds_2, last_five_team2)
    # Izračunavanje skorova za opciju X
    relative_odds_diff = abs(odds_1 - odds_2) / min(odds_1, odds_2)
    bonus_draw = 0.2 * relative_odds_diff  # Bonus se smanjuje sa rastućom razlikom u kvotama
    score_X = (score_1 + score_2) / 2 + bonus_draw

    # Prikaz rezultata
    results = {'1': score_1, 'X': score_X, '2': score_2}
    best_option = max(results, key=results.get)
    print(f"Izračunati koeficijenti su:\nZa Pobedu 1: {score_1:.3f}, za Nerešeno: {score_X:.3f}, za Pobedu 2: {score_2:.3f}")
    print(f'Zato je najbolja opcija za igrati: {best_option}')


if __name__ == "__main__":
    main()
