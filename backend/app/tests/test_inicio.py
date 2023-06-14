from tests.pajinas.inicio import Inicio


def test_carga_pagina_inicio(chrome_page, base_url):
    chrome_page.goto(base_url)
    inicio = Inicio(chrome_page)

    assert inicio.texto_de_ejercisio.inner_text() == "¿Por qué deberías aprender Python?"
    assert inicio.opciones.count() == 4
    assert inicio.ejercisio_id.inner_text() != "9999999"
