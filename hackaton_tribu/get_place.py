import consts
import Screen


# def get_location():
#     recieved_location = "north"
#     recieved_hobby = "sea"
#     return recieved_location, recieved_hobby

def find_place():
    recieved_location = Screen.selection()
    recieved_hobby = Screen.
    for place in consts.DICT_PLACES_VOLUNTEER.items():
        if recieved_location == consts.DICT_PLACES_VOLUNTEER[place][consts.LOCATION_INDEX] and \
                recieved_hobby == consts.DICT_PLACES_VOLUNTEER[place][consts.HOBBY_INDEX]:
            return place


def return_place_info(place):
    return consts.DICT_PLACES_VOLUNTEER[place][consts.INFO_INDEX]

