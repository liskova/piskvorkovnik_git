from random import randrange
from util import tah


def tah_pocitace(pole, symbol_pocitace):
    "Vrátí herní pole se zaznamenaným tahem počítače"

    if symbol_pocitace == "x":
        symbol_hrace = "o"
    else:
        symbol_hrace = "x"

    zkus_hrat_znova = 1
    while zkus_hrat_znova == 1:
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
        else:
            cislo_policka = randrange(0,20)
        if pole[cislo_policka] != "-":  #si řikám, že by se to asi mělo vnořit
            zkus_hrat_znova = 1
        else:
            zkus_hrat_znova = 0

    return tah(pole, cislo_policka, symbol_pocitace)
