import os
os.system('cls')


for i in range(1, 6):
    print(f"tabla del {i}")

    for n in range(1, 11):

        resultado = i * n
        print(f'{i} X {n} = {resultado}')
    print()