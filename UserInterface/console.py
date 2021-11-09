from Domain.vanzare2 import get_gen, get_id, get_pret, get_tip_reducere, get_titlu
from Domain.vanzare2 import creeaza_vanzare, get_str
from Logic.misc import apply_discount, get_list_of_genres, get_lowest_price, get_titles_with_genre, sort_by_price
from Logic.crud import create, read,update,delete
from UserInterface.console2 import run_ui2

def menu():
    print("""
    1. CRUD
    2. Afisare
    3. Schimba genul unei carti
    4. Determina pretul minim pentru fiecare gen
    5. Afișarea numărului de titluri distincte pentru fiecare gen
    6. Aplicarea unui discount de 5% pentru toate reducerile silver și 10% pentru toate reducerile gold
    7. Ordonarea vânzărilor crescător după preț
    undo. Undo
    alt. Instructiuni pe o singura linie
    x. Iesire
    """)

def handle_create(vanzari):
    try:
        id_vanzare = int(input('Dati id ul noii vanzari: '))
        titlu = input('Dati titlul cartii vandute: ')
        gen = input('Dati genul cartii vandute: ')
        pret = int(input('Dati pretul vanzarii: '))
        tip_reducere = input('Dati tipul reducerii (gold, silver sau none): ')
        return create(vanzari,id_vanzare,titlu,gen,pret,tip_reducere)
    except ValueError as err:
        print('Id ul si pretul trebuie sa fie de tip intreg')
        return vanzari

def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))

def handle_update(vanzari):
    try:
        id_vanzare = int(input('Dati id ul vanzarii: '))
        titlu = input('Dati noul titlu al cartii vandute: ')
        gen = input('Dati noul gen al cartii vandute: ')
        pret = int(input('Dati noul pret al vanzarii: '))
        tip_reducere = input('Dati noul tip de reducere (gold, silver sau none): ')
        return update(vanzari,creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_reducere))
    except ValueError as err:
        print('Id ul si pretul trebuie sa fie de tip intreg')
        return vanzari

def handle_delete(vanzari):
    try:
        id_vanzare = int(input('Dati id-ul vanzarii care se va sterge: '))
        return delete(vanzari,id_vanzare)
    except ValueError as err:
        print(err.args[0] + 'Id ul unei vanzari trebuie sa fie un intreg')
        return vanzari

def handle_crud(vanzari, lista_versiuni, versiune_curenta):
    print('a.   Adaugare.')
    print('b.   Modificare.')
    print('c.   Stergere.')
    print('d.   Afisare.')

    optiune = input('Optiune aleasa: ')
    if optiune == 'a':
        vanzari = handle_create(vanzari)
        lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
    elif optiune == 'b':
        vanzari = handle_update(vanzari)
        lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
    elif optiune == 'c':
        vanzari =handle_delete(vanzari)
        lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
    elif optiune == 'd':
        handle_show_all(vanzari)
    else:
        print('Optiune invalida.')
    return vanzari, lista_versiuni, versiune_curenta

def handle_change_genre(vanzari):
    try:
        titlu = input('Dati titlul cartii al carei gen doriti sa il schimbati: ')
        vanzare_de_modificat = None
        for vanzare in vanzari:
            if get_titlu(vanzare) == titlu:
                vanzare_de_modificat = vanzare
        if vanzare_de_modificat == None:
            raise ValueError('Nu exista nicio carte cu acest titlu')
        gen_nou = input('Dati nou gen al catii: ')
        return update(vanzari,creeaza_vanzare(get_id(vanzare_de_modificat),get_titlu(vanzare_de_modificat),gen_nou,get_pret(vanzare_de_modificat),get_tip_reducere(vanzare_de_modificat)))
    except ValueError as val_err:
        print(val_err.args[0])
        return vanzari

def handle_lowest_price(vanzari):
    lista_genuri = get_list_of_genres(vanzari)
    print('Preturile minime pentru genurile existente sunt:')
    for gen in lista_genuri:
        print(f'    -pentru genul {gen}, pretul minim este: {get_lowest_price(gen,vanzari)}')

def handle_distinct_titles(vanzari):
    lista_genuri = get_list_of_genres(vanzari)
    print('Titlurile disponibile sunt urmatoarele:')
    for gen in lista_genuri:
        print(f'    -pentru genul {gen}, titlurile disponibile sunt: {get_titles_with_genre(gen,vanzari)}')

def handle_discount(vanzari):
    lista_vanzari = []
    for el in vanzari:
        discounted_el = apply_discount(el)
        lista_vanzari.append(discounted_el)
    print("Reducerile au fost aplicate cu succes!")
    return lista_vanzari

def handle_order_by_price(vanzari):
    if len(vanzari) > 0:
        lista_ordonata = sort_by_price(vanzari)
        print("Vanzarile ordonate dupa pret crescator sunt:")
        for el in lista_ordonata:
            print(get_str(el))
    else:
        print("Lista de vanzari este goala.")

def handle_undo(lista_versiuni, versiune_curenta):
    if versiune_curenta == 0:
        print("Nu se mai poate face undo")
        return
    versiune_curenta -= 1
    return lista_versiuni[versiune_curenta], versiune_curenta

def handle_add_new_version(vanzare, lista_versiuni, versiune_curenta):
    while versiune_curenta < len(lista_versiuni) - 1:
        lista_versiuni.pop()
    lista_versiuni.append(vanzare)
    versiune_curenta += 1
    return lista_versiuni, versiune_curenta

def run_ui(vanzari):
    lista_versiuni = [vanzari]
    versiune_curenta = 0
    while True:
        menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            vanzari, lista_versiuni, versiune_curenta = handle_crud(vanzari, lista_versiuni, versiune_curenta)
        elif optiune == '2':
            handle_show_all(vanzari)
        elif optiune == '3':
            vanzari = handle_change_genre(vanzari)
            lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
        elif optiune == '4':
            handle_lowest_price(vanzari)
        elif optiune == '5':
            vanzari = handle_distinct_titles(vanzari)
            lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
        elif optiune == '6':
            vanzari = handle_discount(vanzari)
            lista_versiuni, versiune_curenta = handle_add_new_version(vanzari, lista_versiuni, versiune_curenta)
        elif optiune == '7':
            handle_order_by_price(vanzari)
        elif optiune == 'undo':
            vanzari, versiune_curenta = handle_undo(lista_versiuni, versiune_curenta)
        elif optiune == 'alt':
            vanzari = run_ui2(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiunea introdusa nu este valida!')