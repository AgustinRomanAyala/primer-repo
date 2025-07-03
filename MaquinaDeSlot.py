import random

simbolos = ['🍒','🍇', '🍉', '7️']

resultado = (random.choices(simbolos, k=3))

print(f'{resultado[0]} | {resultado[1]} | {resultado[2]}')

if (resultado[0] == '7️' and resultado[1] == '7️' and resultado[2] == '7️'):
  print("Jackpot! 💰")
else:
  print("Gracias por jugar")