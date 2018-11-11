from ai import tah_pocitace
from util import tah
from piskvorky import vyhodnot

def test_tah_pocitace_vyhravat():
    akce = tah_pocitace("-xx-----xx-------oxo")
    assert akce == "xxx-----xx-------oxo"

    akce = tah_pocitace("oxxo---x-x--------oo")
    assert akce == "oxxo---xxx--------oo"

    akce = tah_pocitace("oxx--------------o-o")
    assert akce == "oxxx-------------o-o"


def test_tah_pocitace_branit_hasit1():

    akce = tah_pocitace("-oo-oxoxoxoxxoxoxxoo")
    assert akce == "xoo-oxoxoxoxxoxoxxoo"

    akce = tah_pocitace("oxxo-------------o-o")
    assert akce == "oxxo-------------oxo"

    akce = tah_pocitace("oo--oxoxoxoxxoxoxxoo")
    assert akce == "oox-oxoxoxoxxoxoxxoo"


def test_tah_prvni():
    nove_pole = tah("--------------------", 0, "x")
    assert nove_pole == "x-------------------"
    nove_pole = tah("--------------------", 19, "o")
    assert nove_pole == "-------------------o"

def test_tah_dalsi():
    nove_pole = tah("-xx--o---o---xx-----", 0, "x")
    assert nove_pole == "xxx--o---o---xx-----"
    nove_pole = tah("-xx--o---o---xx-----", 17, "o")
    assert nove_pole == "-xx--o---o---xx--o--"

def test_vyhodnot_bez_vyhry():
    vysledek = vyhodnot("--------------------")
    vysledek = vyhodnot("---------o----------")
    vysledek = vyhodnot("--o---x---o---o-----")
    vysledek = vyhodnot("--o---xx--o---oo----")
    vysledek = vyhodnot("-xooxoxoxxoxxooxoxox")
    assert vysledek == "-"


def test_vyhodnot_vyhry():
    vysledek = vyhodnot("xxx-----------------")
    vysledek = vyhodnot("--ooxxx----------o--")
    vysledek = vyhodnot("xxxoxoxoxoxoxoxoxoxo")
    assert vysledek == "x"

    vysledek = vyhodnot("-----------------ooo")
    vysledek = vyhodnot("xx------ooo-------xx")
    vysledek = vyhodnot("xoooxoxoxoxoxoxoxoxo")
    assert vysledek == "o"

def test_vyhodnot_remiza():
    vysledek = vyhodnot("xxooxoxoxoxoxoxoxoxx")
    assert vysledek == "!"








#assert len(pole) == 20
