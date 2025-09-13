import random

for _ in range(100):
    nove_digitos = []
    for i in range(9):
        digitos = random.randint(1, 9)
        nove_digitos.append(str(digitos))

    separado = [int(digito) for digito in nove_digitos]
    separado_i_1 = 0
    dados_salvos = []
    for vezes in range(10, 1, -1):
        multiplicacao = vezes * separado[separado_i_1]
        dados_salvos.append(multiplicacao)
        separado_i_1 += 1

    soma_tudo = sum(dados_salvos)
    digito_1 = soma_tudo * 10
    digito_1 = digito_1 % 11
    dados_salvos_para_o_digito_2 = []

    separado_i_2 = 0
    if digito_1 > 9:
        digito_1 = 0

    separado.append(digito_1)

    for vezes in range(11, 1, -1):
        multiplicacao_2 = vezes * separado[separado_i_2]
        dados_salvos_para_o_digito_2.append(multiplicacao_2)
        separado_i_2 += 1

    soma_tudo_2 = sum(dados_salvos_para_o_digito_2)
    digito_2 = soma_tudo_2 * 10
    digito_2 = digito_2 % 11

    if digito_2 > 9:
        digito_2 = 0

    cpf_formado = f'{separado}{digito_2}' \
        .replace('[', '') \
        .replace(' ', '') \
        .replace(',', '') \
        .replace(']', '')
    cpf_formado = (f"{cpf_formado[0:3]}."
                   f"{cpf_formado[3:6]}."
                   f"{cpf_formado[6:9]}-"
                   f"{cpf_formado[9:11]}")
    print(f'O seu CPF é {cpf_formado}')