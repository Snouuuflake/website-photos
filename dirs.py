import os
import sys

def get_sub_dirs(path: str):

    resL = []
    
    for entry in os.scandir(path):
        if entry.is_dir():
            resL.append(entry.name)

    return resL


def get_files(path: str):

    resL = []
    
    for entry in os.scandir(path):
        if entry.is_file():
            resL.append(entry.name)

    return resL


def new_dir():
    
    in_name = ""
    valid_name = False

    print("Directorios Existentes:\n")
    
    for i in get_sub_dirs('.'):
        print(i)

    print()

    existing_dirs = get_sub_dirs('.')
    
    while not valid_name:
        valid_name = True
        
        in_name = input("Nombre del nuevo directorio: ")
        
        if in_name.lower() == 'q':
            sys.exit(0)

        for lowered in [element.lower() for element in existing_dirs]:
            if in_name.lower() == lowered and valid_name:
                print("Nombre ya existe, vuelva a intentar o presione 'q' para cerrar el programa.")
                valid_name = False 
    
    os.system(f"mkdir {in_name}")

    return f".\\{in_name}\\"



def load_dir():
    
    in_name = ""
    valid_name = False

    existing_dirs = get_sub_dirs('.')
    
    print("Directorios Existentes:\n")
    
    for i in get_sub_dirs('.'):
        print(i)

    print()

    while not valid_name:
        valid_name = False
        
        in_name = input("Nombre del directorio a cargar: ")
        
        if in_name.lower() == 'q':
            sys.exit(0)

        for lowered in [element.lower() for element in existing_dirs]:
            if in_name.lower() == lowered and not valid_name:
                valid_name = True 
    
        if not valid_name:
            print(f"El nombre {in_name} no existe. Vuelva a intentar o presione 'q' para cerrar el programa")


    return f".\\{in_name}\\"

