from random import randrange
from math import ceil
from util import tah



def tah_pocitace(pole, symbol_pocitace):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if symbol_pocitace == "x":
        symbol_hrace = "o"
    else:
        symbol_hrace = "x"

 #overeni moznosti tahnout
    if "-" not in pole:
        raise ValueError("Není kam hrát, herní pole je buď plné nebo bezrozměrné!")

#tah

    #vyhrávat
    if ("-" + str(2*symbol_pocitace)) in pole:
        cislo_policka = pole.index("-" + str(2*symbol_pocitace))
    elif (str(symbol_pocitace) + "-" + str(symbol_pocitace)) in pole:
        cislo_policka = pole.index(str(symbol_pocitace) + "-" + str(symbol_pocitace))+1
    elif (str(2*symbol_pocitace) + "-") in pole:
        cislo_policka = pole.index(str(2*symbol_pocitace) + "-")+2

    #bránit - hasit1
    elif ("-" + str(2*symbol_hrace)) in pole:
        cislo_policka = pole.index("-" + str(2*symbol_hrace))
    elif (str(symbol_hrace) + "-" + str(symbol_hrace)) in pole:
        cislo_policka = pole.index((str(symbol_hrace)) + "-" + str(symbol_hrace))+1
    elif (str(2*symbol_hrace) + "-") in pole:
        cislo_policka = pole.index(str(2*symbol_hrace) + "-") +2

    #bránit - prasit 1 (PREKLEP -tohle se musí opravit, takhle to nemůže nic dělat)
    elif (("-" + str(symbol_hrace) + "-") in pole) and (("-" + str(symbol_pocitace) + "-") not in pole):
        cislo_policka = pole.index("-" + str(symbol_hrace) + "-")+2

# budovat 1
    elif ("-" + str(symbol_pocitace) + "-") in pole:
        cislo_policka = pole.index("-" + str(symbol_pocitace) + "-")+2

#branit - prasit 2
    elif ("-" + str(symbol_hrace) + "-") in pole:
        cislo_policka = pole.index("-" + str(symbol_hrace) + "-")+2

# budovat 2
    elif "-----" in pole:
        cislo_policka = pole.index("-----") + 3
    elif "---" in pole:
        cislo_policka = pole.index("---") + 1
    elif "-" in pole:
        cislo_policka = pole.index("-")

    # # budouvat 2
    # else:
    #     for kolikrat in range (len(pole), -1, -1):
    #         if (kolikrat*"-") in pole:
    #             cislo_policka = (pole.index(kolikrat*"-") #+ int(kolikrat/2)) + 1



    # # náhoda nakonec
    # else:
    #     zkus_hrat_znova = 1
    #     while zkus_hrat_znova == 1:
    #         cislo_policka = randrange(0, len(pole))
    #         if pole[cislo_policka] != "-":
    #             zkus_hrat_znova = 1
    #         else:
    #             zkus_hrat_znova = 0

    return tah(pole, cislo_policka, symbol_pocitace)
