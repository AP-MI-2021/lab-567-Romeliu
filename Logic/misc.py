from Domain.vanzare2 import get_gen, get_pret, get_titlu, creeaza_vanzare, get_id, get_tip_reducere

def get_lowest_price(gen: str, vanzari) -> int:
    """ 
    :param gen: genul cartilor
    :param vanzari: lista de vanzari
    :return: pretul minim al vanzarilor cu genul dat
    """
    minim = None
    for vanzare in vanzari:
        if get_gen(vanzare) == gen:
            if minim is None:
                minim = get_pret(vanzare)
            elif minim > get_pret(vanzare):
                minim = get_pret(vanzare)
    return  minim

def get_list_of_genres(vanzari) -> list:
    """ 
    :param vanzari: lista de vanzari
    :return: lista de genuri din vanzari
    """
    lista_genuri = []
    for vanzare in vanzari:
        if get_gen(vanzare) not in lista_genuri:
            lista_genuri.append(get_gen(vanzare))
    return lista_genuri

def get_titles_with_genre(gen,vanzari) -> list:
    """ 
    :param gen: genul cartilor
    :param vanzari: lista de vanzari
    :return: lista de titluri cu genul dat
    """
    lista_titluri = []
    for vanzare in vanzari:
        if get_gen(vanzare) == gen:
            lista_titluri.append(get_titlu(vanzare))
    return lista_titluri

def apply_discount(vanzare):
    """ 
    :param vanzari: un obiect de tip vanzare
    :return: un obiect de tip vanzare cu aceleasi atribute ca si parametrul primit, 
            dar cu pretul modificat in functie de tipul de reducere
    """
    reducere = get_tip_reducere(vanzare)
    if reducere == 'gold':
        pret_nou = int(get_pret(vanzare) * (90 / 100))
        return creeaza_vanzare(get_id(vanzare), get_titlu(vanzare), get_gen(vanzare), pret_nou, get_tip_reducere(vanzare))
    elif reducere == 'silver':
        pret_nou = int(get_pret(vanzare) * (95 / 100))
        return creeaza_vanzare(get_id(vanzare), get_titlu(vanzare), get_gen(vanzare), pret_nou, get_tip_reducere(vanzare))
    else:    
        return vanzare

def sort_by_price(vanzari) -> list:
    """ 
    :param vanzari: lista de vanzari
    :return: returneaza lista de vanzari sortata crescator dupa pret
    """
    vanzari_sortate = vanzari.copy()
    vanzari_sortate.sort(key = get_pret)
    return vanzari_sortate