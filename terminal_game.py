import random

print("""🙌 El mundo de Nytherra ha sido fracturado por el surgimiento del Eclipse Silente, 
una fuerza que convierte recuerdos y emociones en enemigos físicos.
Tres elegidos —un Guerrero, una Maga, y un Arquero— son enviados en una misión para sellar el Eclipse
antes de que absorba todo vestigio de humanidad.""")

while True:
     print("1️⃣ Guerrero")
     print("2️⃣ Mago")
     print("3️⃣ Arquero")
     jugar = int(input("Bienvenido a la aventura, elegí tu personaje: "))

     if jugar in [1, 2, 3]:
          break
     else:
          print("Opcion no valida! Elegí nuevamente...")
          
hp = 0
ataque = 0
bloqueo = 0

if jugar == 1:
        hp += 50
        ataque += 17
        bloqueo += 20
        print(f"💪 ¡Bienvenido Colmillo de Hierro! -","vida:",  hp,"daño:", ataque, "bloqueo:", bloqueo)

elif jugar == 2:
          hp += 35
          ataque += 22
          bloqueo += 10 
          print(f"🧙‍♀️ ¡Bienvenido Nova Arcana! -","vida:",  hp,"daño:", ataque, "bloqueo:", bloqueo )

else:
     hp += 40
     ataque += 20
     bloqueo += 15
     print(f"🎯 ¡Bienvenido Ojo de Halcón! -","vida:",  hp,"daño:", ataque, "bloqueo:", bloqueo)



print("""ACTO I:🌄 Comienzas la aventura saliendo del Bosque de la Eternidad. 
Luego de una larga caminata escuchas unos ruidos, 
es una persona de una aldea cercana que quedo atrapada bajo escombros,
¿Lo podras ayudar?""")
print("1️⃣ Lo ayudas a salir")
print("2️⃣ No es tu problema, tenes una misión")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
     hp -= 5
     ataque += 5
     print("👴 ¡El aldeano es rescatado, y te confirma que recordara tu ayuda por siempre!")
     print("Perdes 5 de vida:", hp, "y ganas 5 de daño:", ataque,".")
else:
     hp += 5
     print("No es tu problema, ¡tenes una misión clara!") 
     print("Ganas 5 puntos de vida:", hp,)



print("""🔪 Siguiendo con tu camino ves a los lejos algo que brilla, 
al acercarte podes ver que es una espada rota con centro extrañamente oscuro...""")
print("1️⃣ Agarras la espada, te puede servir en tu viaje")
print("2️⃣ No te da buena sensacion, es preferible dejarla")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
     hp -= 2
     ataque += 5
     bloqueo += 3
     print("👊 Hay que estar siempre preparado!")
     print("Perdes 2 puntos de vida:", hp, "5 puntos de ataque:", ataque, " y 3 de bloqueo:", bloqueo)
else:
     print("Es mejor no complicar el viaje")
     print("Tenes puntos de vida:", hp, "Y puntos de ataque:", ataque)

print(""""😱 Te encontras en el camino con un cuervo gigante que esta herido, te habla,
te ofrece un "atajo" a cambio de ayudarlo... pero no parece de fiar""" )
print("1️⃣ Necesitar toda la ayuda posible, aceptas la propuesta")
print("2️⃣ No podes tomarte la desición rapidamente, es mejor seguir")

jugada = int(input("Selecciona una opción: "))


if jugada == 1:
      
      hp -= 15
      ataque += 7
      print("Perdes 15 puntos de vida:", hp, "Y ganas 7 puntos de ataque:", ataque)
      print("☝ El cuervo cambia buena parte de tu salud y a cambio te da mas fuerza!")

else:
     jugada == 2
     print("No te fias del cuervo, agarras una piedra enorme con todas tus fuerzas")

     piedra = random.randint(0,1)

     if piedra > 0.5:
          ataque += 5
          print("💥 Tiras la piedra, le pegaste en la cabeza, te da su fuerza sin pedirte nada a cambio")
          print("Ganas 5 puntos de ataque:", ataque, "Y tenes", hp, "puntos de vida")
     else:
          hp -= 5
          bloqueo += 2 
          print("💢El cuervo lo esquiva y te golpea, pero apenas te roza")
          print("Perdes 5 puntos de vida:", hp, " Ganas 2 de bloqueo:", bloqueo, "Y tenes", ataque, "puntos de ataque")   

print(""""🏠 Empezas a ver a tu aldea a lo lejos pero todo lo que hay son ruinas,
te preguntas que fue lo que paso, pero en ese mismo momento un gran orco aparece,
pateando y golpeando lo que una vez fue tu hogar.
¡No lo dudas, tomas tu arma y decidis enfrentarlo!""" )
print("1️⃣ Lo atacas de frente con todas tus fuerzas antes de dejarlo reaccionar")
print("2️⃣ Vas con cuidado por la espalda, tenes una oportunidad de hacerle mucho daño")

jugada = int(input("Selecciona una opción: "))


if jugada == 1:
     print("El orco te ve con actitud claramente amenazante y decide pelear")

     pelea = random.randint(1, 3)

     if pelea == 1 and ataque < 20:
          print("💥 lo golpeaste fuertemente, no parece ser rival")
     elif pelea == 2 and ataque > 20:
          hp -=25
          print("💢 El orgo intenta golpearte rapidamente...")
          if bloqueo < 20:
               print("🛡️ Cubriste el daño completamente!")
          else:
               print("Perdes 20 puntos de vida:", hp)
     else:
          hp += 10
          print("🎯 Lo golpeaste en el medio del pecho, su arma y su casco salen volando")
          print("🛡️ Te pones el casco, Ganas 10 puntos de vida:", hp)


if jugada == 2:
     print("Lo tenes justo delante tuyo de espaldas, ES AHORA, lo tenes que atacar!!")
     
     ataque_sorpresa = random.randint(0,1)

     if ataque_sorpresa > 0.5:
          ataque += 5
          print("Le clavas tu daga en la espalda baja, SU PUNTO DEBIL, el orco muere instantaneamente")
          print("Ganas 5 puntos de ataque: ", ataque,  "Y tenes", hp, "puntos de vida")
     elif ataque_sorpresa < 0.5:
          print("Pisas una rama justo un segundo antes de atacar, te escucha y te golpea con todas sus fuerzas")
          if bloqueo < 15:
               print("🛡️ Cubriste el daño completamente!")
          else:
               hp -= 25     
               print("Perdes 20 puntos de vida: ", hp, "Y tenes", ataque, "puntos de ataque") 
     else:
          hp <= 0
          print("💀 Has caído en batalla... El juego ha terminado.")
          exit()
print("🏹 Sobreviviste al encuentro. Sobreviviste al primer acto! El camino continúa...")

print("""ACTO II: 🌫️ Tras vencer al orco, avanzás entre las ruinas humeantes de tu aldea.
Los ecos del pasado se sienten cada vez más cerca... y más reales.
Frente a vos, se abre un sendero de piedras flotantes que lleva a una estructura antigua:
**El Santuario de los Recuerdos**.""")
print("Entrás al santuario con cautela. Las paredes están cubiertas de espejos... pero todos muestran versiones de vos mismo. Uno te habla.")

print("1️⃣ Enfrentás a tu reflejo con furia")
print("2️⃣ Intentás razonar con tu versión oscura")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    ataque += 4
    hp -= 10
    print("💥 Tu reflejo lucha con fuerza, pero lográs vencerlo.")
    print("Ganas 4 puntos de ataque:", ataque, "y perdés 10 de vida:", hp)
else:
    bloqueo += 3
    print("🧘 Lográs calmar al reflejo, que se disuelve en luz.")
    print("Ganas 3 puntos de bloqueo:", bloqueo, "y conservás tus puntos de vida:", hp)


print("""💫 Más adelante, una figura encapuchada aparece: es un antiguo amigo... o lo era.
Ha sido consumido por el Eclipse y no recuerda quién sos.
Te ofrece compartir su poder a cambio de tu lealtad al Eclipse.""")

print("1️⃣ Aceptás su poder")
print("2️⃣ Rechazás su oferta y lo enfrentás")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    ataque += 5
    hp -= 15
    print("🔥 Sentís una fuerza oscura recorrer tu cuerpo.")
    print("Ganas 5 de ataque:", ataque, "pero perdés 15 de vida:", hp)
else:
    ataque += 2
    bloqueo += 2
    print("⚔️ Vencés a tu viejo amigo en un duelo rápido.")
    print("Ganas 2 puntos de ataque:", ataque, "y 2 de bloqueo:", bloqueo)


print("""🪨 Al salir del santuario, un espíritu elemental bloquea el camino.
Te ofrece abrir el paso si resolvés su enigma:
**'Cuanto más le quitás, más grande se vuelve. ¿Qué es?'**""")

print("1️⃣ Respondés: 'Un agujero'")
print("2️⃣ Respondés: 'El silencio'")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    hp += 10
    print("✅ El espíritu asiente y desaparece.")
    print("Ganas 10 puntos de vida:", hp)
else:
    hp -= 5
    bloqueo += 2
    print("❌ El espíritu se enoja, pero te deja pasar con un golpe leve.")
    print("Perdés 5 de vida:", hp, "pero ganás 2 de bloqueo:", bloqueo)


print("""🏚️ Finalmente, salís del templo, pero un enjambre de sombras te rodea.
No son fuertes, pero son muchas.
Tenés solo segundos para decidir tu estrategia.""")

print("1️⃣ Lanzás un ataque explosivo para barrerlos rápido")
print("2️⃣ Usás una técnica defensiva para aguantar y contraatacar")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    if ataque >= 25:
        print("💥 Tu ataque los destruye a todos. Sobreviviste al asalto.")
        hp += 5
    else:
        hp -= 10
        print("⚠️ Matás a varios, pero algunos logran dañarte.")
    print("Puntos de vida actuales:", hp)
else:
    if bloqueo >= 15:
        print("🛡️ Resistís cada golpe y contraatacás con precisión.")
        ataque += 3
    else:
        hp -= 10
        print("💢 Resistís parte del daño, pero algunos ataques te superan.")
    print("Puntos de vida actuales:", hp, "Puntos de ataque:", ataque)

print("🎯 Has superado el segundo acto. El eclipse ruge desde las profundidades...")

print("""ACTO III:🏯 Después de atravesar las ruinas y enfrentar tus sombras internas,
llegás al corazón de Nytherra: la **Torre del Eclipse**, un lugar donde el tiempo y la realidad se distorsionan.
Cada escalón que subís, sentís que tu fuerza y tus recuerdos son puestos a prueba.""")

print("🌀 Una voz te habla desde lo alto: 'Has llegado lejos... ¿Pero sabrás quién sos realmente?'")
print("Frente a vos, tres espejos: uno muestra tu pasado, otro tu presente, y otro... lo que podrías llegar a ser.")

print("1️⃣ Destruís el espejo del futuro: no querés ver lo que viene")
print("2️⃣ Te acercás al espejo del pasado: querés recordar por qué luchás")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    ataque += 3
    print("🔥 Rompés el espejo con furia. El reflejo se disuelve en energía.")
    print("Ganas 3 puntos de ataque:", ataque)
else:
    hp += 10
    bloqueo += 2
    print("🌟 Al mirar tu pasado, te llenás de propósito.")
    print("Ganas 10 de vida:", hp, "y 2 de bloqueo:", bloqueo)


print("""🪞 Más adelante, te enfrentás a tu **yo Eclipse**, una versión corrompida de vos mismo que te habla con tu voz:
'Ya no hay redención, solo poder. Entregate a mí y dominarás lo que nadie ha podido.'""")

print("1️⃣ Lo enfrentás con todo tu poder")
print("2️⃣ Intentás purificarlo y reconciliarte con tu oscuridad")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    if ataque >= 30:
        print("⚔️ Tu poder es abrumador. Vencés a tu sombra sin dejar dudas.")
    else:
        hp -= 15
        print("💢 Luchás con todo, pero salís herido del combate.")
    print("HP actual:", hp)
else:
    if bloqueo >= 15:
        print("🕊️ Canalizás tu energía interna y disipás la corrupción.")
        ataque += 2
    else:
        hp -= 10
        print("El intento fracasa y sos herido por tu propio reflejo.")
    print("HP actual:", hp, "Ataque actual:", ataque)


print("""🌑 Has llegado al último piso. Allí te espera **Umbrenox**, el Eclipse Silente encarnado.
Un ser hecho de sombra pura, nacido de los miedos, odios y dolores de la humanidad.

☁️ Umbrenox: 'Todo lo que amaste se desvanecerá. Dámelo... y te dejaré vivir como mi emisario eterno.'

Decidís qué hacer frente a él:""")

print("1️⃣ Lo atacás con todo lo que te queda")
print("2️⃣ Lo enfrentás, pero intentás sellarlo en lugar de destruirlo")

jugada = int(input("Selecciona una opción: "))

if jugada == 1:
    if ataque >= 35 and hp > 0:
        print("🌟 Tu poder es legendario. Con un grito de guerra, destruís a Umbrenox y liberás Nytherra.")
        print("🏆 **Final Bueno: Libertador del Eclipse**")
    elif ataque >= 25 and hp > 0:
        print("💥 Vencés al Eclipse, pero quedás gravemente herido. Tu historia será leyenda.")
        print("🏅 **Final Gris: Héroe Caído**")
    else:
        print("💀 Tu ataque no es suficiente. Umbrenox te consume.")
        print("❌ **Final Malo: Sombra del Eclipse**")
else:
    if bloqueo >= 20 and hp >= 20:
        print("🕊️ Usás tu poder defensivo para canalizar el sello ancestral.")
        print("🌄 Umbrenox es contenido por tu fuerza espiritual. El Eclipse ha sido sellado.")
        print("🏆 **Final Bueno: Guardián del Alba**")
    elif bloqueo >= 15 and ataque >= 25:
        print("⚖️ Lográs sellarlo, pero quedás atrapado junto a él en el vacío.")
        print("🏅 **Final Gris: Sacrificio Eterno**")
    else:
        print("💀 El intento falla. Umbrenox se alimenta de tu debilidad.")
        print("❌ **Final Malo: Portador del Eclipse**")

input("\nPresioná ENTER para salir...")