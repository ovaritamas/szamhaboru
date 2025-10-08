"""
Számháború játék
Mezei Dávid, Óvári Tamás
2025.10.08
"""

import random as r

print("""
  /$$$$$$                         /$$                 /$$                                    
 /$$__  $$                       | $$                | $$                                    
| $$  \__//$$$$$$$$ /$$$$$$/$$$$ | $$$$$$$   /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$  /$$   /$$
|  $$$$$$|____ /$$/| $$_  $$_  $$| $$__  $$ |____  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  | $$
 \____  $$  /$$$$/ | $$ \ $$ \ $$| $$  \ $$  /$$$$$$$| $$  \ $$| $$  \ $$| $$  \__/| $$  | $$
 /$$  \ $$ /$$__/  | $$ | $$ | $$| $$  | $$ /$$__  $$| $$  | $$| $$  | $$| $$      | $$  | $$
|  $$$$$$//$$$$$$$$| $$ | $$ | $$| $$  | $$|  $$$$$$$| $$$$$$$/|  $$$$$$/| $$      |  $$$$$$/
 \______/|________/|__/ |__/ |__/|__/  |__/ \_______/|_______/  \______/ |__/       \______/ 
""")

nyertes = 0
vesztes = 0
dontetlen = 0

game = True

print("Üdv a számháború játékban!")



while game:

    computer_num = r.randint(1, 7)

    choice = int(input("Kérek egy számot! (1-6): "))
    while choice not in range(1,7):
        print("Kérlek a megadott intervallumból adj meg egy számot!")        
        choice = int(input("Kérek egy számot! (1-6): "))

    if choice < computer_num:
        print("Vesztettél!")
        vesztes += 1
    elif choice > computer_num:
        print("Nyertél")
        nyertes += 1
    elif choice == computer_num:
        print("Döntetlen")
        vesztes += 1

    folyt = input("Szeretnél tovább játszani? (i/n) ")

    if folyt == "n".lower():
        print(f"Vége a játéknak! Nyertes játékok: {nyertes}, Vesztes játékok: {vesztes}, Döntetlen játékok: {dontetlen}")
        game = False
