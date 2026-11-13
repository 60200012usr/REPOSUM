import random

numero_secreto = random.randint(1, 10)
intentos = 3

print("Adivina el número entre 1 y 10. Tienes 3 intentos.")

for i in range(intentos):
    try:
        intento = int(input(f"Intento {i + 1}: "))
    except ValueError:
        print("Escribe un número válido.")
        continue

    if intento == numero_secreto:
        print("¡Correcto! Ganaste 🎉")
        break
    elif intento < numero_secreto:
        print("Es más alto.")
    else:
        print("Es más bajo.")
else:
    print(f"Perdiste. El número era {numero_secreto}.")