import os
import cv2

from dirs import *



def shoot(path, camNum):
    os.system("cls")
    print("Presiona espacio para tomar fotos y esc para salir de la ventana.\n")
    in_char = '-'
    in_name = ""

    cam = cv2.VideoCapture(camNum)

    width = 1920
    height = 1080
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    cv2.namedWindow("Window 1")

    img_counter = 0

    while True:
        ret, frame = cam.read()

        if not ret:
            print("!! failed to grab frame")
            break
        cv2.imshow("Window 1", cv2.resize(frame, (0,0), fx=0.5, fy=0.5))

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Cerrando")
            return 0

        elif k%256 == 32:
            # SPACE pressed
            
            if input("Escriba g para guardar. \n") == 'g':

                in_name = input("Nombre del archivo (referencia): ")
                img_name = f"{in_name}.png"  
                img_path = os.path.join(path,img_name)
                #print("!!!!", img_path)
                if img_name in get_files(path):
                    in_char = '-'
                    while in_char == '-':
                        in_char = '-'
                        in_char = input(f"Archivo {in_name} ya existe. Desea reemplazarlo? s/n: ")

                        if in_char == 's':
                            cv2.imwrite(img_path, frame)
                            print(f"Se guardó imágen: {in_name}")
                        elif in_char == 'n':
                            print("Imagen no se guardó.")
                        else:
                            in_char = '-'

                else:
                    cv2.imwrite(img_path, frame)
                    print(f"Se guardó imágen: {in_name}")

            else:
                print("Imagen no se guardó.")


    cam.release()

cv2.destroyAllWindows()
