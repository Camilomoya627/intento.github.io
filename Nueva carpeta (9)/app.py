import os
from tkinter import Tk, filedialog

def subir_archivo():
    # Abrir la ventana de selección de archivo
    root = Tk()
    root.withdraw()  # Ocultar la ventana de Tkinter
    archivo = filedialog.askopenfilename(title="Seleccione un archivo", filetypes=[("Todos los archivos", "*.*")])

    # Verificar si se seleccionó un archivo
    if archivo:
        # Obtener el nombre del archivo
        nombre_archivo = os.path.basename(archivo)

        # Verificar si la carpeta "upload" existe, si no existe crearla
        carpeta_upload = "upload"
        if not os.path.exists(carpeta_upload):
            os.makedirs(carpeta_upload)

        # Copiar el archivo a la carpeta "upload"
        destino = os.path.join(carpeta_upload, nombre_archivo)
        os.rename(archivo, destino)

        print(f"Archivo '{nombre_archivo}' subido con éxito a la carpeta 'upload'.")

def main():
    while True:
        print("1. Subir archivo")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            subir_archivo()
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()