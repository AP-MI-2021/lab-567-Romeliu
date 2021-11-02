from Domain.vanzare2 import creeaza_vanzare, get_id


def create(lst_obj,id_vanzare,titlu,gen,pret,tip_reducere):
    #creeaza o vanzare noua pe care o adauga in lista de vanzari
    try:
        obiect = creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_reducere)
        return lst_obj + [obiect]
    except ValueError as err:
        print(err.args)
        return lst_obj

def read(lst_obj,id_vanzare:int = None):
    #daca primeste un parametru id_vanzare, citeste vanzarea cu acel id
    #daca nu primeste un id, citeste toata lista de vanzari
    if id_vanzare is not None:
        for obj in lst_obj:
            if id_vanzare == get_id(obj):
                return obj
        raise ValueError('nu exista nicio vanzare cu id-ul dat')
    else:
        return lst_obj

def update(lst_obj,vanzare_noua):
    #returneaza o lista in care vanzarea cu id-ul egal cu id-ul vanzarii noi este inlocuita de aceasta
    lista_noua = []

    for obj in lst_obj:
        if get_id(obj) == get_id(vanzare_noua):
            lista_noua.append(vanzare_noua)
        else:
            lista_noua.append(obj)

    return lista_noua

def delete(lst_obj,id_vanzare:int):
    #returneaza o lista in care se afla toate vanzarile care se aflau in lista initiala, mai putin elementul cu id-ul dat ca parametru

    lista_noua = []

    for obj in lst_obj:
        if get_id(obj) != id_vanzare:
            lista_noua.append(obj)

    return lista_noua