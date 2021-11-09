from Domain.vanzare2 import get_gen, get_pret, get_titlu


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