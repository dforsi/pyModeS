from pyModeS import bds


def test_bds_infer():
    assert bds.infer("8D406B902015A678D4D220AA4BDA") == "BDS08"
    assert bds.infer("8FC8200A3AB8F5F893096B000000") == "BDS06"
    assert bds.infer("8D40058B58C901375147EFD09357") == "BDS05"
    assert bds.infer("8D485020994409940838175B284F") == "BDS09"

    assert bds.infer("A800178D10010080F50000D5893C") == "BDS10"
    assert bds.infer("A0000638FA81C10000000081A92F") == "BDS17"
    assert bds.infer("A0001838201584F23468207CDFA5") == "BDS20"
    assert bds.infer("A0001839CA3800315800007448D9") == "BDS40"
    assert bds.infer("A000139381951536E024D4CCF6B5") == "BDS50"
    assert bds.infer("A00004128F39F91A7E27C46ADC21") == "BDS60"


def test_bds_is50or60():
    assert bds.is50or60("A0001838201584F23468207CDFA5", 0, 0, 0) == None
    assert bds.is50or60("A0000000FFDA9517000464000000", 182, 237, 1250) == "BDS50"
    assert bds.is50or60("A0000000919A5927E23444000000", 413, 54, 18700) == "BDS60"
