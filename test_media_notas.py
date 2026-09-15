from media_notas import calcular_media


def test_calcular_media_com_notas():
    assert calcular_media([8.0, 6.0]) == 7.0


def test_calcular_media_sem_notas():
    assert calcular_media([]) is None


def test_calcular_media_uma_nota():
    assert calcular_media([10.0]) == 10.0


def test_calcular_media_varias_notas():
    assert calcular_media([7.0, 8.0, 9.0]) == 8.0
