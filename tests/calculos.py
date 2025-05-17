def calcular_total_receitas(salario, auxilio, bicos, outros):
    return sum([salario, auxilio, bicos, outros])

def calcular_total_despesas(moradia, alimentacao, transporte, saude, educacao, lazer, outras):
    return sum([moradia, alimentacao, transporte, saude, educacao, lazer, outras])

def calcular_saldo(total_receitas, total_despesas):
    return total_receitas - total_despesas

def gerar_dica_financeira(saldo):
    if saldo > 0:
        return "Parabéns! Você fechou no azul. Tente guardar uma parte como reserva."
    elif saldo < 0:
        return "Você gastou mais do que ganhou. Reveja os gastos não essenciais."
    else:
        return "Você zerou. Que tal economizar um pouco no próximo mês?"
