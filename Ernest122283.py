# Wyświetlenie instrukcji dla użytkownika
print("Wprowadź tekst:")

# Pobranie tekstu od użytkownika
t = input()

# Wyświetlenie wprowadzonego tekstu
print('Wprowadz znak ^ aby wyświetlic liczbe znaków(zdanie musi byc zakonczone kropka):')

# Definicja zbiorów samogłosek, spółgłosek oraz cyfr
sam = 'aeiouyAEIOUY'
spol = 'bcdfghjklmnpqrstvxzwBCDFGHJKLMNPQRSTVXZW'
lp = '1234567890'

# Inicjalizacja zmiennych do przechowywania statystyk
s = 0  # Licznik samogłosek
sp = 0  # Licznik spółgłosek
liczba = 0  # Licznik cyfr
xz = 0  # Licznik znaków specjalnych
lz = 0  # Licznik zdań
liczba_lini = 0  # Licznik wierszy

# Pętla wczytująca kolejne linie tekstu i analizująca je
while t != '^':  # Pętla kończy się po wprowadzeniu znaku "^"
    # Analiza tekstu pod kątem występowania poszczególnych znaków
    for z in t:
        if z in sam:
            s += 1
        elif z in spol:
            sp += 1
        elif z in lp:
            liczba += 1
        elif z not in (' ', '\t', '\n', '^'):
            xz += 1

        # Zliczanie liczby zdań poprzez analizę znaków końca zdania
        if z in ('.', '!', '?'):
            lz += 1

    # Zliczanie liczby wierszy
    if t.strip():  # Sprawdź, czy linia nie jest pusta
        liczba_lini += 1

    # Pobranie kolejnej linii tekstu od użytkownika
    t = input()

# Wyświetlenie zebranych statystyk
print("\n\nSamogłoski=", s)
print("Spółgłoski=", sp)
print("Liczby=", liczba)
print("Znaki specjalne=", xz)
print("Zdania=", lz)
print("Wiersze=", liczba_lini)
