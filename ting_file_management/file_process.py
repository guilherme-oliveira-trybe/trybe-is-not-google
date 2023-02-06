from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for instance in instance.queue:
        if instance["nome_do_arquivo"] == path_file:
            return None

    read_text = txt_importer(path_file)

    file_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(read_text),
        "linhas_do_arquivo": read_text
    }
    instance.enqueue(file_process)

    return sys.stdout.write(str(file_process))


def remove(instance):
    if len(instance.queue) == 0:
        return sys.stdout.write("Não há elementos\n")
    path_file = instance.queue.pop(0)
    return (
        print(f"Arquivo {path_file['nome_do_arquivo']} removido com sucesso\n")
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
