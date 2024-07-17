import streamlit as st


def calculate_weighted_score(odds, last_five_games):
    # Smanjujemo ponderisanje rezultata utakmica
    weights = [3, 2.5, 2, 1.5, 1]
    score = sum([weights[i] * (1 if result == 'W' else 0.50 if result == 'D' else -0.10) for i, result in
                 enumerate(last_five_games)])
    # Uzimamo u obzir i kvotu, gde manja kvota dobija veći skor, ali smanjujemo uticaj rezultata
    weighted_score = (score / odds) * 0.4 + (1 / odds) * 0.6
    print(f"koeficijent na osnovu zadnjih 5 utakmica je {score}")
    print(f"ukupni koeficijent na osnovu utakmica/kvota je {weighted_score}")
    return weighted_score


def main():
    st.title("Radetov Betting kalkulator")

    st.write("Unesite kvote za opcije 1, X i 2 vaše željene utakmice:")

    # Unos kvota
    odds_1 = st.number_input("Kvote za 1:", min_value=1.0, step=0.01)
    odds_X = st.number_input("Kvote za X:", min_value=1.0, step=0.01)
    odds_2 = st.number_input("Kvote za 2:", min_value=1.0, step=0.01)

    st.divider()

    st.write("Unesite rezultate poslednjih 5 utakmica za tim 1 (W, D ili L) i tim 2 (W, D ili L):")

    last_five_team1 = []
    last_five_team2 = []
    goals_team1 = []  # Lista za broj golova za svaku od poslednjih 5 utakmica za tim 1
    goals_team2 = []  # Lista za broj golova za svaku od poslednjih 5 utakmica za tim 2

    col1, col2 = st.columns(2)

    for i in range(5):
        with col1:
            result_team1 = st.radio(f'Rezultat utakmice {i + 1} za tim 1:', ['W', 'D', 'L'], index=2,
                                    key=f'team1_game_{i}')
            goals_team1.append(st.number_input(f'Broj golova za utakmicu {i + 1} za tim 1:', min_value=0, step=1))
            last_five_team1.append(result_team1)
        with col2:
            result_team2 = st.radio(f'Rezultat utakmice {i + 1} za tim 2:', ['W', 'D', 'L'], index=2,
                                    key=f'team2_game_{i}')
            goals_team2.append(st.number_input(f'Broj golova za utakmicu {i + 1} za tim 2:', min_value=0, step=1))
            last_five_team2.append(result_team2)

    st.divider()

    if st.button("Izračunaj"):
        # Izračunavanje ponderisanih skorova
        score_1 = calculate_weighted_score(odds_1, last_five_team1)
        # Prednost domaceg terena
        score_1 += 0.15
        score_2 = calculate_weighted_score(odds_2, last_five_team2)
        # Izračunavanje skorova za opciju X
        relative_odds_diff = abs(odds_1 - odds_2) / min(odds_1, odds_2)
        bonus_draw = 0.2 * relative_odds_diff  # Bonus se smanjuje sa rastućom razlikom u kvotama
        score_X = (score_1 + score_2) / 2 + bonus_draw

        # Provera broja golova u zadnjih 5 utakmica za hint
        total_goals_team1 = sum(goals_team1)
        total_goals_team2 = sum(goals_team2)

        hint1 = ""
        hint2 = ""
        if total_goals_team1 > 11:
            hint1 = f"U zadnjih pet utakmica Tim 1 je postigao {total_goals_team1} golova, razmislite da igrate i na dosta golova"
        elif total_goals_team1 < 5:
            hint1 = f"U zadnjih pet utakmica Tim 1 je postigao {total_goals_team1} gola, razmislite da igrate na malo golova"
        else:
            hint1 = "Ekipa 1 igra normalno bez isticaja povodom broja golova"

        if total_goals_team2 > 11:
            hint2 = f"U zadnjih pet utakmica Tim 2 je postigao {total_goals_team2} golova, razmislite da igrate i na dosta golova"
        elif total_goals_team2 < 5:
            hint2 = f"U zadnjih pet utakmica Tim 2 je postigao {total_goals_team2} gola, razmislite da igrate na malo golova"
        else:
            hint2 = "Ekipa 2 igra normalno bez isticaja povodom broja golova"




        # Prikaz rezultata
        results = {'1': score_1, 'X': score_X, '2': score_2}
        best_option = max(results, key=results.get)
        st.write(
            f"Izračunati koeficijenti su:\nZa Pobedu 1: {score_1:.3f}, za Nerešeno: {score_X:.3f}, za Pobedu 2: {score_2:.3f}")
        st.write(f'Zato je najbolja opcija za igrati: {best_option}')
        st.write(f'Napomena: {hint1}')
        st.write(f'Napomena: {hint2}')


if __name__ == "__main__":
    main()