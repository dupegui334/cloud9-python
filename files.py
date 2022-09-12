from os import scandir

def crear_file():
    with open('datos.txt','w') as file: #open or create the file, and w of write to give permissions of writing, and assign it to file.
        datos = 'Algunos datos que voy a escribir en mi archivo'
        file.write(datos)


def leer_file():
    with open('datos.txt','r') as archivo:
        print(archivo.read())


def scan_content_dir():#Print dirs and files
    with scandir("/home/ec2-user/environment") as directorios:
        for direct in directorios:
            print(direct.name)
            

def scan_content_file():# print only files
    with scandir("/home/ec2-user/environment") as directorios:
        for direct in directorios:
            if direct.is_file():
                print(direct.name)

if __name__=='__main__':
    crear_file()
    leer_file()
    scan_content_dir()
    scan_content_file()