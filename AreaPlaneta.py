from math import pi
from random import choice as ch

planets = [
  'Mercurio',
  'Venus',
  'Tierra',
  'Marte',
  'Saturno'
]

planeta_random = ch(planets)


if planeta_random == 'Mercurio':
  radio = 2440
elif planeta_random == 'Venus':
  radio = 6052
elif planeta_random == 'Tierra':
  radio = 6371
elif planeta_random == 'Marte':
  radio = 3390
elif planeta_random == 'Saturno':
  radio = 58232
else:
  print("Nooo, cualquier cosa!")

area = 4 * pi * radio ** 2

print(f'Planeta: {planeta_random} Area: {area}')