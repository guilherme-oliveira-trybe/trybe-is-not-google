import sys


def txt_importer(path_file):
    try:
        if path_file.endswith(".txt"):
            with open(path_file) as file:
                read_file = file.read().splitlines()
                return read_file

        return sys.stderr.write("Formato inválido")
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
