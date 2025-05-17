from .calculos import calcular_total_receitas, calcular_total_despesas, calcular_saldo, gerar_dica_financeira

def test_calcular_total_receitas():
    assert calcular_total_receitas(1000, 200, 300, 400) == 1900

def test_calcular_total_despesas():
    assert calcular_total_despesas(100, 200, 300, 400, 500, 600, 700) == 2800

def test_calcular_saldo():
    assert calcular_saldo(5000, 3000) == 2000
    assert calcular_saldo(3000, 3000) == 0
    assert calcular_saldo(2000, 3000) == -1000

def test_gerar_dica_financeira():
    assert gerar_dica_financeira(100) == "Parabéns! Você fechou no azul. Tente guardar uma parte como reserva."
    assert gerar_dica_financeira(-50) == "Você gastou mais do que ganhou. Reveja os gastos não essenciais."
    assert gerar_dica_financeira(0) == "Você zerou. Que tal economizar um pouco no próximo mês?"
