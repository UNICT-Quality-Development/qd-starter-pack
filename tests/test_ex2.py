from src.ex2 import giorno_della_settimana


def test_giorno_della_settimana():
    assert giorno_della_settimana(1) == "Lunedì"
    assert giorno_della_settimana(2) == "Martedì"
    assert giorno_della_settimana(3) == "Mercoledì"
    assert giorno_della_settimana(4) == "Giovedì"
    assert giorno_della_settimana(5) == "Venerdì"
    assert giorno_della_settimana(6) == "Sabato"
    assert giorno_della_settimana(7) == "Domenica"
    assert giorno_della_settimana(0) == "--"
    assert giorno_della_settimana(8) == "--"
