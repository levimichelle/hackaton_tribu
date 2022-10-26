import tkinter
import region_screen
import hobby_screen
import consts


def find_place():
    received_location = region_screen.region_screen()
    received_hobby = hobby_screen.hobby_screen()
    for place in consts.lst_of_keys:
        if received_location == consts.DICT_PLACES_VOLUNTEER[place][consts.LOCATION_INDEX] and\
                received_hobby == consts.DICT_PLACES_VOLUNTEER[place][consts.HOBBY_INDEX]:
            specific_place = place
            return specific_place


def return_place_info():
    place = find_place()
    return consts.DICT_PLACES_VOLUNTEER[place][consts.INFO_INDEX]


def show_volunteering():
    app = tkinter.Tk()
    app.title("Volunteer Quiz")
    app.geometry("350x350+500+100")
    app.configure(bg="lightblue")
    place_name = find_place()
    place_info = return_place_info()
    label1 = tkinter.Label(app, text=f"We found you a volunteering place!\n {place_name}", bg="lightblue", font=("David", 24))
    label1.pack(pady=20)
    label2 = tkinter.Label(app, text=place_info, bg="lightblue", font=("David", 18))
    label2.pack(pady=20)
    app.mainloop()

