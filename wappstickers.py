import os
import sys
import time


def change_extension(folder):
    for filename in os.listdir(folder):
        # import pdb; pdb.set_trace()
        infilename = os.path.join(folder,filename)
        oldbase = os.path.splitext(filename)
        newname = infilename.replace(oldbase[1], '.webp')
        output = os.rename(infilename, newname)
    return output


def print_usage_and_exit(program_name):
    sys.stderr.write('Uso: %s  <path_a_carpeta> \n' % program_name)
    options = '''
        <carpeta> = Path a la carpeta de archivos a transformar
        Ejemplo: C:\\Users\\Pepe\\Desktop\\prueba
        '''
    sys.stderr.write(options)
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage_and_exit(sys.argv[0])
    folder = sys.argv[1]

    try:
        print('Iniciando cambio de extension de archivos')
        change_extension(folder)
        time.sleep(1)
        print('Listo, termine!')
    except KeyboardInterrupt:
        sys.stderr.write('Noooooo! no me dejas terminar! Apretaste ctrl+c O--O\n')
