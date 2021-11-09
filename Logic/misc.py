from Domain.vanzare2 import get_gen, get_pret, get_titlu, creeaza_vanzare, get_id, get_tip_reducere

def get_lowest_price(gen,vanzari):
    minim = None
    for vanzare in vanzari:
        if get_gen(vanzare) == gen:
            if minim is None:
                minim = get_pret(vanzare)
            elif minim > get_pret(vanzare):
                minim = get_pret(vanzare)
    return  minim

def get_list_of_genres(vanzari):
    lista_genuri = []
    for vanzare in vanzari:
        if get_gen(vanzare) not in lista_genuri:
            lista_genuri.append(get_gen(vanzare))
    return lista_genuri

def get_titles_with_genre(gen,vanzari):
    lista_titluri = []
    for vanzare in vanzari:
        if get_gen(vanzare) == gen:
            lista_titluri.append(get_titlu(vanzare))
    return lista_titluri

def apply_discount(vanzare):
    reducere = get_tip_reducere(vanzare)
    if reducere == 'gold':
        pret_nou = int(get_pret(vanzare) * (90 / 100))
        return creeaza_vanzare(get_id(vanzare), get_titlu(vanzare), get_gen(vanzare), pret_nou, get_tip_reducere(vanzare))
    elif reducere == 'silver':
        pret_nou = int(get_pret(vanzare) * (95 / 100))
        return creeaza_vanzare(get_id(vanzare), get_titlu(vanzare), get_gen(vanzare), pret_nou, get_tip_reducere(vanzare))
    else:    
        return vanzare

def sort_by_price(vanzari):
    vanzari_sortate = vanzari.copy()
    vanzari_sortate.sort(key = get_pret)
    return vanzari_sortate