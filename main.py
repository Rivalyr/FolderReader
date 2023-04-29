from colorama import Fore
import shutil
import time
import os


cmd = lambda cmdl: os.system(cmdl)
cmplist = []
exelist = []
piclist = []
doclist = []
vidlist = []
audiolist = []


file_extension = {
    'CompressedFile': ['rar', 'zip', '7z', 'gzip', 'tar'],
    'Executable': ['exe', 'msi', 'bat'],
    'Pictures': ['png', 'jpg', 'jpeg', 'jfif', 'svg', 'gif', 'webp'],
    'Audio': ['mp3', 'flac', 'aac', 'wav', 'ogg'],
    'Video': ['mp4', 'm4a', 'avi', 'mov', 'webm'],
    'Documents': ['pdf', 'doc', 'docx', '.xlsx']
}


def folderchecker(path):
    os.chdir(path)

    # Check if necessary folders exist
    for folder in list(file_extension.keys()):
        if not os.path.isdir(os.path.join(path, folder)):
            print('\nLa carpeta no existe.')
            cmd(f'mkdir {folder}')
            print('\tCreando carpeta...')
            time.sleep(0.5)
            cmd('cls')

    cmd('cls')
    time.sleep(2)
    print('Folder check: Successful')


def filefilter(path):
    files = os.listdir(path)

    for file in files:
        """Starting here, the program will verify if any of the extensions (specified in the dictionary on line 16) are present 
        in the file. If any are found, the program will proceed to move all files to the designated folder for that file type."""
        try:
            if file.endswith(tuple(file_extension.get('Executable'))):
                shutil.move(file, os.path.join(path, 'Executable'))
                exelist.append(file)

            elif file.endswith(tuple(file_extension.get('CompressedFile'))):
                shutil.move(file, os.path.join(path, 'CompressedFile'))
                cmplist.append(file)

            elif file.endswith(tuple(file_extension.get('Pictures'))):
                shutil.move(file, os.path.join(path, 'Pictures'))
                piclist.append(file)

            elif file.endswith(tuple(file_extension.get('Audio'))):
                shutil.move(file, os.path.join(path, 'Audio'))
                audiolist.append(file)

            elif file.endswith(tuple(file_extension.get('Video'))):
                shutil.move(file, os.path.join(path, 'Video'))
                vidlist.append(file)

            elif file.endswith(tuple(file_extension.get('Documents'))):
                shutil.move(file, os.path.join(path, 'Documents'))
                doclist.append(file)
        except shutil.Error:
            print('Algun archivo ya ha sido movido o ya existe en esa ruta.')


if __name__ == '__main__':
    # Path that u wanna order.
    pathorg = r'C:\Users\Riva\Downloads'
    # pathorg = os.getcwd()

    # From here its gonna check if u have the needed folders
    folderchecker(pathorg)

    # Now lets filter all the files
    filefilter(pathorg)
    print(f'{Fore.CYAN}Total files moved: {Fore.RESET}{len(cmplist + doclist + vidlist + audiolist + piclist + exelist)}')
