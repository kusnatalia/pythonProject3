def suma_listy(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_listy(lista[1:])

# Proces:
# - Jeżeli lista jest pusta to zwracamy 0
# - Jesli jest inaczej to zwracamy pierwszy element listy, dodany do sumy reszty listy
# - Wywołujemy funkcję rekurencyjnie dla skróconej listy - bez pierwszego elementu

def znajdz_najwiekszy_element_listy(lista):
   if len(lista) == 1:
       return lista[0]
   else:
       pierwszy_element = lista[0]
       reszta_listy = lista[1:]
       najwiekszy_w_reszcie = znajdz_najwiekszy_element_listy(reszta_listy)
       return max(pierwszy_element, najwiekszy_w_reszcie)


# Proces:
# - Jeżeli lista ma tylko jeden element, zwracamy ten element.
# - W przeciwnym razie, dzielimy listę na pierwszy element i resztę listy.
# - Rekurencyjnie znajdujemy największy element w reszcie listy.
# - Porównujemy pierwszy element z największym elementem w reszcie i zwracamy większy z nich.

def silnia(s):
   if s == 0:
       return 1
   else:
       return s * silnia(s-1)


# Proces:
# Jeżeli s wynosi 0, zwracamy 1 (warunek końcowy)
#  Jeśli nie, zwracamy iloczyn s i silni z (s-1)
# Wywołujemy funkcję rekurencyjnie dla liczby mniejszej o 1

def fib(f):
   if f <= 1:
       return f
   else:
       return fib(f-1) + fib(f-2)


# Proces:
# Jeżeli f jest mniejsze lub równe 1, zwracamy f (warunek końcowy)
# W przeciwnym razie, zwracamy sumę dwóch poprzednich liczb ciągu Fibonacciego
# Wywołujemy funkcję rekurencyjnie dla dwóch poprzednich liczb

def rozwiaz_sudoku(sudoku):
    if not czy_sa_puste_pola(sudoku):
        return sudoku

    m, n = znajdz_nastepne_puste_pole(sudoku)

    for i in range(1, 5):
        if czy_poprawna_liczba(sudoku, m, n, i):
            sudoku[m][n] = i

            if rozwiaz_sudoku(sudoku):
                return sudoku

            sudoku[m][n] = 0

    return None


def czy_sa_puste_pola(sudoku):
    for row in sudoku:
        if 0 in row:
            return True
    return False


def znajdz_nastepne_puste_pole(sudoku):
    for m in range(4):
        for n in range(4):
            if sudoku[m][n] == 0:
                return m, n


def czy_poprawna_liczba(sudoku, m, n, num):
    # Sprawdzanie wiersza
    for i in range(4):
        if sudoku[m][i] == num:
            return False

    # Sprawdzanie kolumny
    for i in range(4):
        if sudoku[i][n] == num:
            return False

    # Sprawdzanie kwadratu 2x2
    start_row = m - m % 2
    start_col = n - n % 2
    for i in range(2):
        for j in range(2):
            if sudoku[start_row + i][start_col + j] == num:
                return False

    return True

# Proces:
# - Sprawdzamy, czy są puste pola w sudoku.
# - Jeśli nie ma żadnych pustych pól, zwracamy rozwiązane sudoku.
# - W przeciwnym razie, znajdujemy następne puste pole.
# - Próujemy wstawić liczby od 1 do 4 i sprawdzamy, czy są poprawne.
# - Jeśli liczba jest poprawna, umieszczamy ją w sudoku i rekurencyjnie wywołujemy funkcję dla pozostałych pustych pól.
# - Jeśli otrzymamy poprawne rozwiązanie, zwracamy sudoku.
# - Jeśli nie otrzymamy rozwiązania, cofamy się do poprzedniego kroku i próbujemy z inną liczbą.
# - Jeżeli wszystkie liczby od 1 do 4 zostały sprawdzone i nie otrzymaliśmy rozwiązania, zwracamy None.


