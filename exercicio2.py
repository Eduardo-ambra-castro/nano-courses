import os
os.system("cls")

# Exercício 02
'''
  Viajar é bom demais! Uma agência de viagens está propondo uma estratégia para alavancar as vendas após os impactos da pandemia do coronavírus.

  A empresa ofertará descontos progressivos na compra de pacotes, dependendo do número de viajantes que estão no mesmo grupo e moram na mesma residência.

  Para ajudar a tornar esse projeto real, você deve criar um algoritmo que receba o VALOR BRUTO do pacote, a CATEGORIA DOS ASSENTOS no vôo e a QUANTIDADE DE VIAJANTES que moram em uma mesma casa e calcule os descontos de acordo com a tabela abaixo:

  Categoria DESCONTOS
  - Econômica       2 viajantes -> 3%
                    3 viajantes -> 4%
                    4 viajantes ou mais -> 5%

  - Executiva       2 viajantes -> 5%
                    3 viajantes -> 7%
                    4 viajantes ou mais -> 8%

  - Primeira classe       2 viajantes -> 10%
                          3 viajantes -> 15%
                          4 viajantes ou mais -> 20%
                    
  O programa deverá exibir o valor BRUTO DA VIAGEM (o mesmo que foi digitado), o VALOR DE DESCONTO, o VALOR LÍQUIDO DA VIAGEM (valor bruto menos os descontos) e o VALOR MÉDIO POR VIAJANTE.
'''

valor_bruto = float(input("Por favor, informe o valor da viagem: "))
cat = input("Por favor, informe a categoria: ECONOMICA, EXECUTIVA ou PRIMEIRA CLASSE: ").strip().upper()
qtd_passageiros = int(input("Qual a quantidade de passageiros? "))

valor_desconto = 0

if cat == "ECONOMICA":
    if qtd_passageiros == 2:
        valor_desconto = valor_bruto * 0.03
    elif qtd_passageiros == 3:
        valor_desconto = valor_bruto * 0.04  # Corrigido para '='
    elif qtd_passageiros >= 4:
        valor_desconto = valor_bruto * 0.05  # Corrigido para '='

elif cat == "EXECUTIVA":
    if qtd_passageiros == 2:
        valor_desconto = valor_bruto * 0.05
    elif qtd_passageiros == 3:
        valor_desconto = valor_bruto * 0.07
    elif qtd_passageiros >= 4:
        valor_desconto = valor_bruto * 0.08

elif cat == "PRIMEIRA CLASSE":
    if qtd_passageiros == 2:
        valor_desconto = valor_bruto * 0.10
    elif qtd_passageiros == 3:
        valor_desconto = valor_bruto * 0.15
    elif qtd_passageiros >= 4:
        valor_desconto = valor_bruto * 0.20

else:
    print("Categoria inexistente")

valor_liquido = valor_bruto - valor_desconto

if qtd_passageiros > 0:
    media_viajantes = valor_liquido / qtd_passageiros
else:
    media_viajantes = 0

print("O valor da viagem é de R${:.2f}. Após os descontos de R${:.2f}, a "
      "viagem custará R${:.2f}. Cada passageiro tem um custo médio de "
      "R${:.2f}".format(valor_bruto, valor_desconto, valor_liquido, media_viajantes))