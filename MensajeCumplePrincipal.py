import datetime, mensajes_cumple

hoy = datetime.date.today()

diacumple = datetime.date(2026, 1, 13)

diasrestantes = diacumple - hoy

if hoy == diacumple:
    print(mensajes_cumple.random_message)
else:
    print(f"Mi Proximo cumpleaños es en : {diasrestantes}")