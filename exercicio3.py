'''
  Hora de decidir! Os colaboradores da sua equipe foram sorteados para ganharem um console de última geração cada um por conta do bom desempenho que tiveram nos último projetos. Por uma questão de logística, porém, a empresa pede que toodos os 5 membros da equipe recebam o mesmo aparelho.

  Crie um algoritmo que o usuário possa digitar o voto de cada um dos 5 membros da equipe e, ao final, exiba qual foi o console escolhido e com quantos votos.

  As opções são:
  - PLAYSTATION
  - XBOX
  - NINTENDO
'''
import os
os.system("cls")

playstation = 0
xbox = 0
nintendo = 0

voto1 = input("Digite o seu voto: ").upper()
voto2 = input("Digite o seu voto: ").upper()
voto3 = input("Digite o seu voto: ").upper()
voto4 = input("Digite o seu voto: ").upper()
voto5 = input("Digite o seu voto: ").upper()

if voto1 == "PLAYSTATION":
  playstation = playstation + 1

elif voto1 == "XBOX":
  xbox = xbox + 1

elif voto1 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 1 digitou um console inexistente e seu voto foi anulado.")

if voto2 == "PLAYSTATION":
  playstation = playstation + 1

elif voto2 == "XBOX":
  xbox = xbox + 1

elif voto2 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 2 digitou um console inexistente e seu voto foi anulado.")

if voto3 == "PLAYSTATION":
  playstation = playstation + 1

elif voto3 == "XBOX":
  xbox = xbox + 1

elif voto3 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 3 digitou um console inexistente e seu voto foi anulado.")


if voto4 == "PLAYSTATION":
  playstation = playstation + 1

elif voto4 == "XBOX":
  xbox = xbox + 1

elif voto4 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 4 digitou um console inexistente e seu voto foi anulado.")

if voto5 == "PLAYSTATION":
  playstation = playstation + 1

elif voto5 == "XBOX":
  xbox = xbox + 1

elif voto5 == "NINTENDO":
  nintendo = nintendo + 1

else:
  print("O colaborador 5 digitou um console inexistente e seu voto foi anulado.")


if playstation > xbox and playstation > nintendo:
  print("O console escolhido foi: PLAYSTATION!")

elif xbox > playstation and xbox > nintendo:
  print("O console escolhido foi: XBOX!")

elif nintendo > playstation and nintendo > xbox:
  print("O console escolhido foi: NINTENDO!")

else:
  print("Houve empate, favor entrar em contato com a direção.")


