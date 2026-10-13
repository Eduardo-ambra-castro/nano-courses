import os
os.system("cls")

'''
  Verificar se os batimentos cardíacos por minuto se encontram na faixa adequada.

  Para isso, você deve solicitar que o usuário informe o seu número de BATIMENTOS POR MINUTO (BPM) e a IDADE.

  A partir disso o script deve verificar e exibir uma mensagem informando se os batimentos do usuário encontram-se DENTRO da faixa adequada, ACIMA da faixa adequada ou ABAIXO da faixa adequada, de acordo com o site "Tua Saúde" (https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm](https://www.tuasaude.com/frequencia-cardiaca/#:~:text=At%C3%A9%202%20anos%20de%20idade,idosos%3A%2050%20a%2060%20bpm):

  IDADE                     BPM
  - Até 2 anos              120 a 140
  - De 8 anos até 17 anos   80 a 100
  - Adulto sedentário       70 a 80
  - Idosos                  50 a 60
'''

print("verificador de frequencias cardiacas")
bpm = int(input("Informe o seu batimento cardiaco: "))
idade = int(input("Informe a sua idade: "))

if idade <= 2:
    if bpm >= 120:
      if bpm <= 140:
        print("Batimentos normais para a idade fornecida")
      else:
        print("Batimentos acima dos indicados para a idade fornecida")
    else:
            print("Batimentos abaixo dos indicados para a idade fornecida")

elif idade >= 8 and idade <= 17:
    if bpm >= 80:
      if bpm <= 100:
        print("Batimentos normais para a idade fornecida")
      else:
        print("Batimentos acima dos indicados para a idade fornecida")
    else:
            print("Batimentos abaixo dos indicados para a idade fornecida")

elif idade >= 18 and idade <= 60:
    if bpm >= 70:
      if bpm <= 80:
        print("Batimentos normais para a idade fornecida")
      else:
        print("Batimentos acima dos indicados para a idade fornecida")
    else:
            print("Batimentos abaixo dos indicados para a idade fornecida")

elif idade <= 60:
    if bpm >= 50:
      if bpm <= 60:
        print("Batimentos normais para a idade fornecida")
      else:
        print("Batimentos acima dos indicados para a idade fornecida")
    else:
            print("Batimentos abaixo dos indicados para a idade fornecida")




