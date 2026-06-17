import os
os.system('cls')


personas = [
    ("Eiver", 23),
    ("Eliana", 25),
    ("Moises", 22),
    ("Andres", 17),
    ("Roberto", 67)
]

print("---- TU PROGRAMA DE EDADES XD ----")

for nombre, edad in personas:
    if edad < 18:
        categoria = 'menor'
    elif edad < 65:
        categoria = "Adulto"
    else:
        categoria = "Mayor"
    
    print(f"{nombre} tiene {edad} años y se clasifica como: {categoria}")
