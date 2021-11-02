from Domain.vanzare2 import creeaza_vanzare, get_gen, get_id, get_pret
from Logic.comparisons import get_lowest_price
from Logic.crud import create, delete, read, update


def get_data():
    return[
        creeaza_vanzare(1,'titlu1','basm',100,'silver'),
        creeaza_vanzare(2,'titlu2','nuvela',23,'gold'),
        creeaza_vanzare(3,'titlu3','poezie',40,'none'),
        creeaza_vanzare(4,'titlu4','basm',140,'gold'),
    ]

def test_create():
    vanzari = get_data()
    vanzare_noua = creeaza_vanzare(5,'t5','bam',52,'silver')
    vanzari2 = create(vanzari,5,'t5','bam',52,'silver')
    assert len(vanzari) == len(vanzare_noua) - 1
    assert vanzare_noua in vanzari2

def test_read():
    vanzari = get_data()
    sample = vanzari[3]
    assert read(vanzari,get_id(sample)) == sample
    assert read(vanzari) == vanzari

def test_update():
    vanzari = get_data()
    vanzare_updated = creeaza_vanzare(3,'t3','bam',52,'gold')
    vanzari_updated = update(vanzari, vanzare_updated)
    assert vanzare_updated in vanzari_updated
    assert vanzare_updated not in vanzari
    assert len(vanzari_updated) == len(vanzari)

def test_delete():
    vanzari = get_data()
    id_deleted = 4
    vanzare_deleted = read(vanzari,id_deleted)
    lista_deleted = delete(vanzari, id_deleted)
    assert vanzare_deleted in vanzari
    assert vanzare_deleted not in lista_deleted
    assert len(vanzari) == len(lista_deleted) + 1

def test_get_minim():
    vanzari = get_data()
    assert get_lowest_price(get_gen(vanzari[0]),vanzari) <= get_pret(vanzari[0])
    assert type(get_lowest_price(get_gen(vanzari[1]),vanzari)) is int

def test_crud():
    test_create()
    test_read()
    test_update
    test_delete()
    test_get_minim()