# Kysymysmodulin testit

# Modulien ja kirjastojen lataukset
import kysymys

# Syöte OK
def test_kysymys_ok():
    assert kysymys.kysy_liukuluku("Syötä arvo", 10, 100) == [0, 'Syöte OK', ]
# Syötteessä tietotyyppivirhe

# Alle alarajan

# Yli ylärajan