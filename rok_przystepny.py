"""
Program sprawdza czy podany rok jest przestępny
"""
def rok_przystepny(year_of_test):
    # wprowadzenie danych wejściowych
    # obliczenia
    # wyrażenie zwraca wartość logiczną
    czy_przestepny = (year_of_test % 400 == 0) or (year_of_test % 100 != 0) and (year_of_test % 4 == 0)

    # wypisanie wyniku
    print('Czy rok', year_of_test, 'jest przestępny?', czy_przestepny)

    return czy_przestepny


if __name__ == '__main__':
    rok = int(input("Podaj rok"))
    rok_przystepny(rok)

def test_rok_ma_byc_przystepny():
    assert rok_przystepny(2020) == True

def test_rok_ma_byc_nieprzystepny():
    assert rok_przystepny(2022) == False