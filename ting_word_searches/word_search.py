def exists_word(word, instance):
    text_exists_word = []
    for path in instance.queue:
        ocorrencias = []
        for i, linha in enumerate(path["linhas_do_arquivo"]):
            if word in linha.lower():
                ocorrencias.append({"linha": i + 1})
        if len(ocorrencias) > 0:
            text_exists_word.append({
                "palavra": word,
                "arquivo": path["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return text_exists_word


def search_by_word(word, instance):
    text_exists_word = []
    for path in instance.queue:
        ocorrencias = []
        for i, linha in enumerate(path["linhas_do_arquivo"]):
            if word in linha.lower():
                ocorrencias.append({"linha": i + 1, "conteudo": linha})
        if len(ocorrencias) > 0:
            text_exists_word.append({
                "palavra": word,
                "arquivo": path["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            })
    return text_exists_word
