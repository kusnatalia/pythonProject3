def suma_listy(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_listy(lista[1:])

# Proces:
# - Jeżeli lista jest pusta to zwracamy 0
# - Jesli jest inaczej to zwracamy pierwszy element listy, dodany do sumy reszty listy
# - Wywołujemy funkcję rekurencyjnie dla skróconej listy - bez pierwszego elementu

