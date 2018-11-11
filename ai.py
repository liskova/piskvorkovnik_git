from random import randrange
from util import tah


def tah_pocitace(pole):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    symbol_pocitace = "x"

    zkus_hrat_znova = 1
    while zkus_hrat_znova == 1:
        #vyhrávat
        if "-xx" in pole:
            cislo_policka = pole.index("-xx")
        elif "x-x" in pole:
            cislo_policka = pole.index("x-x")+1
        elif "xx-" in pole:
            cislo_policka = pole.index("xx-")+2
        #bránit - hasit1
        elif "-oo" in pole:
            cislo_policka = pole.index("-oo")
        elif "o-o" in pole:
            cislo_policka = pole.index("o-o")+1
        elif "oo-" in pole:
            cislo_policka = pole.index("oo-")+2
        else:
            cislo_policka = randrange(0,20)
        if pole[cislo_policka] != "-":  #si řikám, že by se to asi mělo vnořit
            zkus_hrat_znova = 1
        else:
            zkus_hrat_znova = 0

    return tah(pole, cislo_policka, symbol_pocitace)
