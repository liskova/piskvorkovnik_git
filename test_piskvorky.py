from ai import tah_pocitace
from util import tah
from piskvorky import vyhodnot

def test_tah_pocitace_vyhravat():
    akce = tah_pocitace("-xx-----xx-------oxo", "x")
    assert akce == "xxx-----xx-------oxo"

    akce = tah_pocitace("oxxo---x-x--------oo", "x")
    assert akce == "oxxo---xxx--------oo"

    akce = tah_pocitace("oxx--------------o-o", "x")
    assert akce == "oxxx-------------o-o"

    akce = tah_pocitace("oxx--------------o-o", "o")
    assert akce == "oxx--------------ooo"


def test_tah_pocitace_branit_hasit1():

    akce = tah_pocitace("-oo-oxoxoxoxxoxoxxoo", "x")
    assert akce == "xoo-oxoxoxoxxoxoxxoo"

    akce = tah_pocitace("oxxo-------------o-o", "x")
    assert akce == "oxxo-------------oxo"

    akce = tah_pocitace("oo--oxoxoxoxxoxoxxoo", "x")
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
    vysledek = vyhodnot("--------------------", "x")
    vysledek = vyhodnot("---------o----------", "x")
    vysledek = vyhodnot("--o---x---o---o-----", "x")
    vysledek = vyhodnot("--o---xx--o---oo----", "o")
    vysledek = vyhodnot("-xooxoxoxxoxxooxoxox", "o")
    assert vysledek == "-"


def test_vyhodnot_vyhry():
    vysledek = vyhodnot("xxx-----------------", "x")
    vysledek = vyhodnot("--ooxxx----------o--", "o")
    vysledek = vyhodnot("xxxoxoxoxoxoxoxoxoxo", "o")
    assert vysledek == "x"

    vysledek = vyhodnot("-----------------ooo", "x")
    vysledek = vyhodnot("xx------ooo-------xx", "o")
    vysledek = vyhodnot("xoooxoxoxoxoxoxoxoxo", "o")
    assert vysledek == "o"

def test_vyhodnot_remiza():
    vysledek = vyhodnot("xxooxoxoxoxoxoxoxoxx", "x")
    assert vysledek == "!"








#assert len(pole) == 20
