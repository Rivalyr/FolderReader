import os
import time
from colorama import Fore


musica = []
ejecutables = []
imagenes = []
compress = []
carpetas = 0


def main():
    global carpetas
    # ruta = str(input('Ruta a la que quieres acceder: '))
    ruta = r'C:\Users\Riva\Downloads'
    os.chdir(r'{}'.format(ruta))
    for file in os.listdir(ruta):

        if file.endswith('.exe') or file.endswith('.msi') or file.endswith('.bat'):
            ejecutables.append(file)

        elif file.endswith('.png') or file.endswith('.jfif') or file.endswith('jpg'):
            imagenes.append(file)

        elif file.endswith('.mp3') or file.endswith('.flac') or file.endswith('.aac') or file.endswith('.wav') or \
                file.endswith('.m4a'):
            musica.append(file)

        elif file.endswith('.7z') or file.endswith('.zip') or file.endswith('.rar') or file.endswith('.tar') or file.endswith(
                '.gz'):
            compress.append(file)

        elif os.path.isdir(os.path.join(ruta, file)):
            carpetas += 1

        else:
            pass
    return carpetas


main()
cmd = lambda command: os.system(command)
imprimir = True
cmd('cls')
while imprimir:
    print(f'\nHay en total: '
          f'{len(ejecutables)} Ejecutables. '
          f'{len(imagenes)} Imagenes. '
          f'{len(musica)} Archivos de audio. '
          f'{len(compress)} Archivos comprimidos. '
          f'Y {carpetas} carpeta(s).')

    infoshow = int(input('¿Quieres mostrar los archivos?'
                         '\n\t1. Mostrar Ejecutables'
                         '\n\t2. Mostrar imagenes'
                         '\n\t3. Mostrar Musica'
                         '\n\t4. Mostrar Archivos comprimidos'
                         '\n\t0. Salir\n=> '))
    match infoshow:
        case 1:
            cmd('cls')
            for exe in ejecutables:
                print(f'{Fore.GREEN} {exe} {Fore.RESET}')

            print(f'\nArchivos totales: {len(ejecutables)}\n')
        case 2:
            cmd('cls')
            for pic in imagenes:
                print(f'{Fore.GREEN} {pic} {Fore.RESET}')

            print(f'\nArchivos totales: {len(imagenes)}\n')
        case 3:
            cmd('cls')
            for song in imagenes:
                print(f'{Fore.GREEN} {song} {Fore.RESET}')

            print(f'\nArchivos totales: {len(musica)}\n')
        case 4:
            cmd('cls')
            for compressed in compress:
                print(f'{Fore.YELLOW} {compressed} {Fore.RESET}')
            print(f'\nArchivos totales: {len(compress)}\n')
        case 0:
            cmd('cls')
            print('Saliendo...')
            time.sleep(1)
            cmd('cls')
            break
        case _:
            print('Valor no valido')
            break
