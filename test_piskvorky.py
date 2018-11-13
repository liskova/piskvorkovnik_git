from ai import tah_pocitace
from util import tah
from piskvorky import vyhodnot

def test_tah_pocitace_vyhravat():
    akce = tah_pocitace("-xx-----xx-------oxo", "x", "o")
    assert akce == "xxx-----xx-------oxo"

    akce = tah_pocitace("oxxo---x-x--------oo", "x", "o")
    assert akce == "oxxo---xxx--------oo"

    akce = tah_pocitace("oxx--------------o-o", "x", "o")
    assert akce == "oxxx-------------o-o"

    akce = tah_pocitace("oxx--------------o-o", "o", "x")
    assert akce == "oxx--------------ooo"


def test_tah_pocitace_branit_hasit1():

    akce = tah_pocitace("-oo-oxoxoxoxxoxoxxoo", "x", "o")
    assert akce == "xoo-oxoxoxoxxoxoxxoo"

    akce = tah_pocitace("oxxo-------------o-o", "x", "o")
    assert akce == "oxxo-------------oxo"

    akce = tah_pocitace("oo--oxoxoxoxxoxoxxoo", "x", "o")
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
    vysledek = vyhodnot("--------------------", "x", "o")
    vysledek = vyhodnot("---------o----------", "x", "o")
    vysledek = vyhodnot("--o---x---o---o-----", "x", "o")
    vysledek = vyhodnot("--o---xx--o---oo----", "o", "x")
    vysledek = vyhodnot("-xooxoxoxxoxxooxoxox", "o", "x")
    assert vysledek == "-"


def test_vyhodnot_vyhry():
    vysledek = vyhodnot("xxx-----------------", "x", "o")
    vysledek = vyhodnot("--ooxxx----------o--", "o", "x")
    vysledek = vyhodnot("xxxoxoxoxoxoxoxoxoxo", "o", "x")
    assert vysledek == "x"

    vysledek = vyhodnot("-----------------ooo", "x", "o")
    vysledek = vyhodnot("xx------ooo-------xx", "o", "x")
    vysledek = vyhodnot("xoooxoxoxoxoxoxoxoxo", "o", "x")
    assert vysledek == "o"

def test_vyhodnot_remiza():
    vysledek = vyhodnot("xxooxoxoxoxoxoxoxoxx", "x", "o")
    assert vysledek == "!"








#assert len(pole) == 20
