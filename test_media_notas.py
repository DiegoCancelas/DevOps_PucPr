from media_notas import calcular_media


def test_calcular_media_com_notas():
    registros = [{"nota": 8.0}, {"nota": 6.0}]
    assert calcular_media(registros) == 7.0


def test_calcular_media_sem_notas():
    assert calcular_media([]) is None


def test_calcular_media_uma_nota():
    registros = [{"nota": 10.0}]
    assert calcular_media(registros) == 10.0
