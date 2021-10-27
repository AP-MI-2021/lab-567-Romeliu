from Domain.vanzare import creeaza_vanzare, get_str
from Logic.crud import create,update,delete

def menu():
    print("""
    1. CRUD
    2. Afisare
    x. Iesire
    """)

def handle_create(vanzari):
    id_vanzare = int(input('Dati id ul noii vanzari'))
    titlu = input('Dati titlul cartii vandute')
    gen = input('Dati genul cartii vandute')
    pret = int(input('Dati pretul vanzarii'))
    tip_reducere = input('Dati tipul reducerii (gold, silver sau none)')
    return create(vanzari,id_vanzare,titlu,gen,pret,tip_reducere)

def handle_show_all(vanzari):
    for vanzare in vanzari:
        print(get_str(vanzare))

def handle_update(vanzari):
    id_vanzare = int(input('Dati id ul vanzarii'))
    titlu = input('Dati noul titlu al cartii vandute')
    gen = input('Dati noul gen al cartii vandute')
    pret = int(input('Dati noul pret al vanzarii'))
    tip_reducere = input('Dati noul tip de reducere (gold, silver sau none)')
    return update(vanzari,creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_reducere))

def handle_delete(vanzari):
    id_vanzare = int(input('Dati id-ul vanzarii care se va sterge:'))
    return delete(vanzari,id_vanzare)



def handle_crud(vanzari):
    while True:
        print('a.   Adaugare.')
        print('b.   Modificare.')
        print('c.   Stergere.')
        print('d.   Afisare.')
        print('x.   Inapoi')

        optiune = input('Optiune aleasa: ')
        if optiune == 'a':
            obiecte = handle_create(vanzari)
        elif optiune == 'b':
            obiecte = handle_update(vanzari)
        elif optiune == 'c':
            obiecte =handle_delete(vanzari)
        elif optiune == 'd':
            handle_show_all(vanzari)
        elif optiune == 'x':
            return True
        else:
            print('Optiune invalida.')

def run_ui(vanzari):
    while True:
        menu()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
            vanzari = handle_crud(vanzari)
        elif optiune == '2':
            handle_show_all(vanzari)
        elif optiune == 'x':
            break
        else:
            print('Optiunea introdusa nu este valida!')