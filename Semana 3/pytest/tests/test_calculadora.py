from utilidades.calculadora import Calculadora


def test_sumar():
    calculadora = Calculadora()
    resultado = calculadora.sumar(2, 3)
    assert resultado == 5


def test_restar():
    calculadora = Calculadora()
    resultado = calculadora.restar(5, 2)
    assert resultado == 3


def test_multiplicar():
    calculadora = Calculadora()
    resultado = calculadora.multiplicar(4, 2)
    assert resultado == 8


def test_dividir():
    calculadora = Calculadora()
    resultado = calculadora.dividir(10, 2)
    assert resultado == 5


def test_dividir_por_cero():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.dividir(10, 0)
