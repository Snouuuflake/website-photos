import os
import sys
import cv2

from dirs import *
from shoot import *

# ---- making gui ----

# initializing gui
def init_gui():
    os.system("cls")


# menu
def menu():
    op = -1
    in_str = ""
    valid_op = False


    print("Menú de Inicio:\n", "1. Nuevo Directorio\n", "2. Cargar Directorio\n", "3. Salir\n", "4. changeCamIndex\n")


    while not valid_op:
        
        in_str = input("Opción: ")

        if in_str.isdigit():
            op = int(in_str)
        else:
            op = -1


        if op > 0 and op < 5:
            valid_op = True

        else:
            print(f"{in_str} no es una opción válida.")


    return op        


# swaps contents of camIndex.txt between 0 and 1
def changeCamIndex(cI):
    f = open("camIndex.txt", "w")
    
    if cI == 0:
        f.write("1")
    elif cI == 1:
        f.write("0")
    else:
        print("\nError: camIndex is not between 0 & 1. Please report.\n")

    f.close()

# returns camIndex.txt's
def getCamIndex():
    f = open("camIndex.txt", "r")
    res = int(f.read(1))
    f.close()
    return res



# --------------- main ---------------
running = True
mainpath = ""
option = 0

camIndex = getCamIndex()
print(f"\ncamIndex: {camIndex}\n")

option = menu()


if option == 1:
    mainpath = new_dir()
    shoot(mainpath, camIndex)
elif option == 2:
    mainpath = load_dir()
    shoot(mainpath, camIndex)
elif option == 3:
    sys.exit(0)
elif option == 4:
    changeCamIndex(camIndex)
else:
    print("how did this happen?")



