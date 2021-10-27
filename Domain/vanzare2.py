def creeaza_vanzare(id_vanzare,titlu,gen,pret,tip_reducere):
    '''
    Creeaza o vanzare
    :param id_vanzare: id-ul vanzarii, unic, nenul
    :param titlu: titlul cartii vandute
    :param gen: genul in care se incaqdreaza cartea vanduta
    :param pret: pretul vanzarii
    :param tip_reducere: tipul reducerii: gold, silver sau none
    '''
    return(id_vanzare,titlu,gen,pret,tip_reducere)

def get_id(obiect):
    #returneaza id-ul obiectului dat ca parametru
    return obiect[0]

def get_titlu(obiect):
    #returneaza titlul cartii vandute
    return obiect[1]

def get_gen(obiect):
    #returneaza genul cartii vandute
    return obiect[2]

def get_pret(obiect):
    #returneaza pretul vanzarii
    return obiect[3]

def get_tip_reducere(obiect):
    #returneaza tipu reducerii aplicate vanzarii
    return obiect[4]

def get_str(obiect):
    return f'Vanzarea cu id-ul; {get_id(obiect)}, cartea vanduta: {get_titlu(obiect)}, din genul {get_gen(obiect)}, pret vanzare: {get_pret(obiect)}, cu reducere aplicata: {get_tip_reducere(obiect)}'