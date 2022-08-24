def duplicate_count(text):
    lista = []
    lista[:0] = text
    masde1 = []
    for t in lista:
        masde1.append(lista.count(t))
    for t in masde1:
        if t < 2:
            masde1.remove(t)
    return len(masde1)


print(duplicate_count("arbOkktJ5HIMBxu1LQ6YuH47AUyZgrYsHgIe2v3p9QQCWXMvMg1UP8kfq9G7gscMTUj9"))
