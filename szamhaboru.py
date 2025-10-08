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
while game:     
    try:
        # A felhasználó beadott adatait kezeljük

        choices = input("Kérek egy számot!(1-6) ")

        while choices.lower() not in [1, 2, 3, 4, 5, 6]:
            print("Kérlek megfelelő választ adj meg!")
            choices = input("Kérek egy számot!(1-6) ")



