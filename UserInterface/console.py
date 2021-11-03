from Domain.vanzare2 import get_gen, get_id, get_pret, get_tip_reducere, get_titlu
from Domain.vanzare2 import creeaza_vanzare, get_str
from Logic.comparisons import get_lowest_price
from Logic.crud import create, read,update,delete
from UserInterface.console2 import run_ui2

def menu():
    print("""
    1. CRUD
    2. Afisare
    3. Schimba genul unei carti
    4. Determina pretul minim pentru fiecare gen
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

def handle_crud(vanzari):
    while True:
        print('a.   Adaugare.')
        print('b.   Modificare.')
        print('c.   Stergere.')
        print('d.   Afisare.')
        print('x.   Inapoi')

        optiune = input('Optiune aleasa: ')
        if optiune == 'a':
            vanzari = handle_create(vanzari)
        elif optiune == 'b':
            vanzari = handle_update(vanzari)
        elif optiune == 'c':
            vanzari =handle_delete(vanzari)
        elif optiune == 'd':
            handle_show_all(vanzari)
        elif optiune == 'x':
            return vanzari
        else:
            print('Optiune invalida.')

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
    lista_genuri = []
    for vanzare in vanzari:
        if get_gen(vanzare) not in lista_genuri:
            lista_genuri.append(get_gen(vanzare))
    print('Preturile minime pentru genurile existente sunt:')
    for gen in lista_genuri:
        print(f'    -pentru genul {gen}, pretul minim este: {get_lowest_price(gen,vanzari)}')

def run_ui(vanzari):
    while True:
        menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == '2':
            handle_show_all(vanzari)
        elif optiune == '3':
            vanzari = handle_change_genre(vanzari)
        elif optiune == '4':
            handle_lowest_price(vanzari)
        elif optiune == 'alt':
            vanzari = run_ui2(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiunea introdusa nu este valida!')