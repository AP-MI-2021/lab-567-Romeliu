from Domain.vanzare2 import creeaza_vanzare, get_gen, get_pret
from Logic.misc import get_list_of_genres, get_lowest_price, get_titles_with_genre

def get_data():
    return[
        creeaza_vanzare(1,'titlu1','basm',100,'silver'),
        creeaza_vanzare(2,'titlu2','nuvela',23,'gold'),
        creeaza_vanzare(3,'titlu3','poezie',40,'none'),
        creeaza_vanzare(4,'titlu4','basm',140,'gold'),
    ]

def test_get_minim():
    vanzari = get_data()
    assert get_lowest_price(get_gen(vanzari[0]),vanzari) <= get_pret(vanzari[0])
    assert type(get_lowest_price(get_gen(vanzari[1]),vanzari)) is int

def test_get_list_of_genres():
    vanzari = get_data()
    assert len(get_list_of_genres(vanzari)) <= len(vanzari)
    if len(vanzari) > 0:
        assert len(get_list_of_genres(vanzari)) > 0

def test_get_titles_with_genre():
    vanzari = get_data()
    if len(vanzari) > 0:
        assert len(get_titles_with_genre(get_gen(vanzari[0]), vanzari)) <= len(vanzari)
        assert len(get_titles_with_genre(get_gen(vanzari[0]),vanzari)) > 0

def test_misc():
    test_get_minim()
    test_get_list_of_genres()
    test_get_titles_with_genre()