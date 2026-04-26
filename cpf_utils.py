import random


def calcular_digito(digitos, multiplicador_inicial):
    soma = sum(valor * multiplicador for valor, multiplicador in zip(digitos, range(multiplicador_inicial, 1, -1)))
    digito = (soma * 10) % 11
    return digito if digito <= 9 else 0


def gerar_numero_cpf():
    nove_digitos = [random.randint(0, 9) for _ in range(9)]
    digito_1 = calcular_digito(nove_digitos, 10)
    digito_2 = calcular_digito(nove_digitos + [digito_1], 11)
    return nove_digitos + [digito_1, digito_2]


def formatar_cpf(cpf):
    cpf_str = ''.join(map(str, cpf))
    return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"