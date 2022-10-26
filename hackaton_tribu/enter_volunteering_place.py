import employer_screen
import consts

def enter_volunteering_place():
    place_name = employer_screen.enter_place_name()
    place_location = employer_screen.enter_place_location()
    place_hobby = employer_screen.enter_place_hobby()
    place_info = employer_screen.enter_place_info()
    lst_values = [place_location, place_hobby, place_info]
    consts.DICT_PLACES_VOLUNTEER[place_name]: lst_values





