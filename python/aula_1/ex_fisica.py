import os
os.system("cls")
'''
isso limpa as infos do terminal

'''
'''
caucular a velocidade media
'''

# pedir a distancia da viagem
dist = float(input("Informe a distancia da viagem (em km): "))

# pedir o tempo da viagem
temp = float(input("Informe o tempo da viagem (em hrs): "))

# caucular o delta da velocidade
delta = dist / temp

#exibir o resultado final
print(f"Sua velocidade media foi {delta:.2f} km/h" )
