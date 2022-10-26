import consts
import Screen


# def get_location():
#     recieved_location = "north"
#     recieved_hobby = "sea"
#     return recieved_location, recieved_hobby

def find_place():
    received_location = Screen.region_screen()
    received_hobby = Screen.hobby_screen()
    for place in consts.lst_of_keys:
        if received_location == consts.DICT_PLACES_VOLUNTEER[place][consts.LOCATION_INDEX] and\
                received_hobby == consts.DICT_PLACES_VOLUNTEER[place][consts.HOBBY_INDEX]:
            return place


def return_place_info():
    place = find_place()
    return consts.DICT_PLACES_VOLUNTEER[place][consts.INFO_INDEX]

