"""
Számháború játék
Mezei Dávid, Óvári Tamás
2025.10.08
"""

import random as r

print("""
 *      _________              .__          ___.                       
 *     /   _____/_______ _____ |  |__ _____ \_ |__   ___________ __ __ 
 *     \_____  \\___   //     \|  |  \\__  \ | __ \ /  _ \_  __ \  |  \
 *     /        \/    /|  Y Y  \   Y  \/ __ \| \_\ (  <_> )  | \/  |  /
 *    /_______  /_____ \__|_|  /___|  (____  /___  /\____/|__|  |____/ 
 *            \/      \/     \/     \/     \/    \/                    
""")

game = True

print("Üdv a számháború játékban!")
choices = [1, 2, 3, 4, 5, 6]


computer_num = r.randint(1-7)

while True:

        choice = int(input("Kérek egy számot! (1-6): "))
        if choice not in choices:
            print("Kérlek, a megadott tartományban adj meg számot!")
            continue
        break  # Kilépünk a ciklusból, mert helyes számot kaptunk


if choice < computer_num:
    print("Vesztettél!")

elif choice > computer_num:
    print("Vesztettél")

elif choice == computer_num:
    print("Döntetlen")

folyt = input("Szeretnél tovább játszani?(i/n) ")