"""
Program sprawdza czy podany rok jest przestępny
"""
def sprawdz_rok(rok):
    # obliczenia
    # wyrażenie zwraca wartość logiczną
    czy_przestepny = (rok % 400 == 0) or (rok % 100 != 0) and (rok % 4 == 0)

    # wypisanie wyniku
    print('Czy rok', rok, 'jest przestępny?', czy_przestepny)

    return czy_przestepny


if __name__ == '__main__':
    # wprowadzenie danych wejściowych
    rok = int(input('Podaj rok: '))
    sprawdz_rok(rok)


def test_czy_rok_przystepny():
    assert sprawdz_rok(2020) == True


def test_czy_rok_nie_przystepny():
    assert sprawdz_rok(2018) == False
