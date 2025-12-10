import random

secreto = random.randint(1, 20)

for i in range(1, 6):
    intento = int(input(f"Intento {i}: Adivina el número del 1 al 20: "))
    
    if intento == secreto:
        print("¡Correcto! Adivinaste el número")
        break
    elif intento < secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")
else:
    # Este else se ejecuta solo si el bucle for termina SIN break
    print(f"No quedan más intentos. El número secreto era {secreto}")
