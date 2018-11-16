from ai import tah_pocitace
from util import tah

def tah_hrace(pole, symbol_hrace):
    """
    dostane řetězec s herním polem, zeptá se hráče,
    na kterou pozici chce hrát, a vrátí herní pole se
    zaznamenaným tahem hráče. Funkce by měla odmítnout
    záporná nebo příliš velká čísla a tahy na obsazená
    políčka. Pokud uživatel zadá špatný vstup, funkce mu
    vynadá a zeptá se znova.
    """

    zeptej_se_znova = 1
    while zeptej_se_znova == 1:
        cislo_policka = int(input("Zadej číslo volné pozice, na kterou chces hrát od 0 do 19."))

        if cislo_policka not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
            print("Tohle by nešlo, číslo políčka musí být 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 nebo 19.")
            zeptej_se_znova = 1

        elif pole[cislo_policka] != "-":
            print("Tohle by nešlo, políčko ", cislo_policka, "je obsazené. Zkus to znovu.")
            zeptej_se_znova = 1

        else:
            zeptej_se_znova = 0


    return tah(pole, cislo_policka, symbol_hrace)

def vyhodnot(herni_retezec, symbol_pocitace):
    """
    dostane řetězec s herním polem 1-D piškvorek a vrátí jednoznakový řetězec podle stavu hry:
    "x" – Vyhrál hráč s křížky (pole obsahuje "xxx") - v aktuální verzi, nahrazeno symbolem_pocitace
    "o" – Vyhrál hráč s kolečky (pole obsahuje "ooo")
    "!" – Remíza (pole neobsahuje "-", a nikdo nevyhrál)
    "-" – Ani jedna ze situací výše (t.j. hra ještě neskončila)
    """
    if symbol_pocitace == "x":
        symbol_hrace = "o"
    else:
        symbol_hrace = "x"


    if str(3*symbol_pocitace) in herni_retezec:
        vyhodnoceni_stavu = str(symbol_pocitace)
    elif str(3*symbol_hrace) in herni_retezec:
        vyhodnoceni_stavu = str(symbol_hrace)
    elif "-" not in herni_retezec:
        vyhodnoceni_stavu = "!"
    else:
        vyhodnoceni_stavu = "-"
    return vyhodnoceni_stavu

def piskvorky1d(symbol_za_ktery_hraje_pocitac):
    if symbol_za_ktery_hraje_pocitac == "x":
        symbol_za_ktery_hraje_hrac = "o"
    else:
        symbol_za_ktery_hraje_hrac = "x"

    aktualni_pole = 20*"-"
    for deset_tahu_staci in range(10):
        print("01234567890123456789")
        aktualni_pole = tah_pocitace(aktualni_pole, symbol_za_ktery_hraje_pocitac)
        print(aktualni_pole)
        print(vyhodnot(aktualni_pole, symbol_za_ktery_hraje_pocitac))
        if vyhodnot(aktualni_pole, symbol_za_ktery_hraje_pocitac) in [symbol_za_ktery_hraje_pocitac,"o", "!"]:
            break
        aktualni_pole = tah_hrace(aktualni_pole, symbol_za_ktery_hraje_hrac)
        print(aktualni_pole)
        print(vyhodnot(aktualni_pole, symbol_za_ktery_hraje_pocitac))
        if vyhodnot(aktualni_pole, symbol_za_ktery_hraje_pocitac) in [symbol_za_ktery_hraje_pocitac,"o", "!"]:
            break
