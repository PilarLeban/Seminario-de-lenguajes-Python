import random
category = {"Lenguajes": ["python", "java", "pascal"],
    "Elementos de un codigo": ["programa", "variable", "funcion", "bucle"],
    "Tipos de datos": ["cadena", "entero", "lista"]
} 
print("Categorías disponibles: ")
for i in category: 
    print(i)
choice = input("Elegí una categoría: ")
if (choice not in category):
    print("No existe esa categoría.")
    exit()
words = random.sample(category[choice], len(category[choice]))
print("¡Bienvenido al Ahorcado!")
print()
for word in words:
    guessed = []
    attempts = 6
    print(f"Comienzo de ronda de la categoría {choice}: ")
    score = 0
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ").strip().lower()
        if len(letter) != 1 or not letter.isalpha(): 
            print('Entrada no válida')
            continue    
        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print() 
    else:
        print(f"¡Perdiste! La palabra era: {word}")  
        score = 0    
    print(f"El puntaje final es: {score}")
