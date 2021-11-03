from Domain.vanzare2 import creeaza_vanzare, get_id, get_pret, get_str, get_tip_reducere, get_titlu

from Logic.crud import create, delete, update


def help():
    print("""
    Optiunile disponibile sunt:
    1. add -    add,int(id),str(titlu),str(gen),int(pret),str(tip_reducere)
                ex: add,1,poezie,basm,15,gold
    2. update - update,int(id),str(titlu),str(gen),int(pret),str(tip_reducere)
                ex: update,1,harap alb,basm,20,silver
    3. remove - remove,int(id)
                ex: remove,1
    4. showall
    5. change_genre -   change_genre,str(titlu),str(new_genre)
                        ex: change_genre,harap alb,basm popular
    Comenzile sunt separate prin ';'
    """)

def show_menu2():
    print("""
    1. help
    2. dati comenzi
    x. exit
    """)

def handle_add(vanzari,parametrii):
    try:
        id_vanzare = int(parametrii[1])
        titlu_vanzare = parametrii[2]
        genul_cartii = parametrii[3]
        pret_vanzare = int(parametrii[4])
        tip_reducere = parametrii[5]
        return create(vanzari,id_vanzare,titlu_vanzare,genul_cartii,pret_vanzare,tip_reducere)
    except ValueError as err:
        print('Id ul si pretul trebuie sa fie de tip intreg')
        return vanzari
    except IndexError:
        print('Va rugam sa atribuiti parametrii corespunzatori comenzilor!')

def handle_update(vanzari,parametrii):
    try:
        id_vanzare = int(parametrii[1])
        titlu_vanzare = parametrii[2]
        genul_cartii = parametrii[3]
        pret_vanzare = int(parametrii[4])
        tip_reducere = parametrii[5]
        return update(vanzari,creeaza_vanzare(id_vanzare,titlu_vanzare,genul_cartii,pret_vanzare,tip_reducere))
    except ValueError:
        print('Id ul si pretul trebuie sa fie de tip intreg')
        return vanzari
    except IndexError:
        print('Va rugam sa atribuiti parametrii corespunzatori comenzilor!')

def handle_remove(vanzari,parametrii):
    try:
        id_vanzare = int(parametrii[1])
        return delete(vanzari,id_vanzare)
    except ValueError:
        print('Id ul unei vanzari trebuie sa fie un intreg')
        return vanzari
    except IndexError:
        print('Va rugam sa atribuiti parametrii corespunzatori comenzilor!')

def handle_showall(vanzari):
    try:
        for vanzare in vanzari:
            print(get_str(vanzare))
    except TypeError:
        print('Lista de vanzari este goala!')

def handle_change_genre(vanzari,parametrii):
    try:
        titlu = parametrii[1]
        vanzare_de_modificat = None
        for vanzare in vanzari:
            if get_titlu(vanzare) == titlu:
                vanzare_de_modificat = vanzare
        if vanzare_de_modificat == None:
            raise ValueError('Nu exista nicio carte cu acest titlu')
        gen_nou = parametrii[2]
        return update(vanzari,creeaza_vanzare(get_id(vanzare_de_modificat),get_titlu(vanzare_de_modificat),gen_nou,get_pret(vanzare_de_modificat),get_tip_reducere(vanzare_de_modificat)))
    except ValueError as val_err:
        print(val_err.args[0])
        return vanzari
    except IndexError:
        print('Va rugam sa atribuiti parametrii corespunzatori comenzilor!')

def run_ui(vanzari):
    while True:
        show_menu2()
        optiune = input('Introduceti optiunea: ')
        if optiune == '1':
           help()
        elif optiune == 'x':
            break
        elif optiune == '2':
            instructiuni = input('Introduceti instructiunile: ')
            lista_instructiuni = instructiuni.split(';')
            for instructiune in lista_instructiuni:
                parametrii = instructiune.split(',')
                comanada = parametrii[0]
                if comanada == 'add':
                    vanzari = handle_add(vanzari,parametrii)
                elif comanada == 'update':
                    vanzari = handle_update(vanzari,parametrii)
                elif comanada == 'remove':
                    vanzari = handle_remove(vanzari,parametrii)
                elif comanada == 'showall':
                    handle_showall(vanzari)
                elif comanada == 'change_genre':
                    vanzari = handle_change_genre(vanzari,parametrii)
                else:
                    if comanada != "":
                        print('Instructiunea introdusa nu este valida!')
        else:
            print('Optiunea introdusa nu este valida!')