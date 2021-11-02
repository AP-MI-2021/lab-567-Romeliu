from Domain.vanzare2 import get_gen, get_pret


def get_lowest_price(gen,vanzari):
    minim = None
    for vanzare in vanzari:
        if get_gen(vanzare) == gen:
            if minim is None:
                minim = get_pret(vanzare)
            elif minim > get_pret(vanzare):
                minim = get_pret(vanzare)
    return  minim