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
