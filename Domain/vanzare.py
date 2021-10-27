def creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_reducere):
    '''
    Creeaza o vanzare
    :param id_vanzare: id-ul vanzarii, unic, nenul
    :param titlu: titlul cartii vandute
    :param gen: genul in care se incaqdreaza cartea vanduta
    :param pret: pretul vanzarii
    :param tip_reducere: tipul reducerii: gold, silver sau none
    '''
    return{
        'id_vanzare':id_vanzare,
        'titlu_carte':titlu,
        'gen_carte':gen,
        'pret_vanzare':pret,
        'tip_reducere':tip_reducere
    }

def get_id(obiect):
    #returneaza id-ul obiectului dat ca parametru
    return obiect['id_vanzare']

def get_titlu(obiect):
    #returneaza titlul cartii vandute
    return obiect['titlu_carte']

def get_gen(obiect):
    #returneaza genul cartii vandute
    return obiect['gen_carte']

def get_pret(obiect):
    #returneaza pretul vanzarii
    return obiect['pret_vanzare']

def get_tip_reducere(obiect):
    #returneaza tipu reducerii aplicate vanzarii
    return obiect['tip_reducere']

def get_str(obiect):
    return f'Vanzarea cu id-ul; {get_id(obiect)}, cartea vanduta: {get_titlu(obiect)}, din genul {get_gen(obiect)}, pret vanzare: {get_pret(obiect)}, cu reducere aplicata: {get_tip_reducere(obiect)}'

def modifica(obiect,key,value):
    #modifica campul key al obiecrului, atribuindu-i valoarea value
    obiect[key] = value