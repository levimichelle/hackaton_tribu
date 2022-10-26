import tkinter
import get_place


# from tkinter import messagebox

def set_screen():
    app = tkinter.Tk()
    app.title("Volunteer Quiz")
    app.geometry("400x400+500+100")
    app.configure(bg="lightblue")
    return app


def introduction_screen():
    app = set_screen()
    label1 = tkinter.Label(app, text="Welcome to TribuApp!\n press 'next' to continue", bg="lightblue", font=("David", 20))
    button = tkinter.Button(app, text="next", command=app.destroy, font=("David", 12))
    label1.pack(pady=20)
    button.pack(side="bottom")


def region_screen():
    app = set_screen()
    var = tkinter.IntVar()
    label1 = tkinter.Label(app, text="What region are you from?", bg="lightblue", font=("David", 20))
    button = tkinter.Button(app, text="next", command=app.destroy, font=("David", 12))
    label1.pack(pady=20)
    button.pack(side="bottom")
    north_button = tkinter.Radiobutton(app, text="north", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=1, font=("David", 14)).pack(anchor=tkinter.CENTER)

    center_button = tkinter.Radiobutton(app, text="center", bg="lightblue", variable=var, pady=5, padx=30,
                                        value=2, font=("David", 14)).pack(anchor=tkinter.CENTER)

    south_button = tkinter.Radiobutton(app, text="south", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=3, font=("David", 14)).pack(anchor=tkinter.CENTER)
    num = str(var.get())
    if num == "1":
        return "north"
    elif num == "2":
        return "center"
    elif num == "3":
        return "south"
    app.mainloop()


def hobby_screen():
    app = set_screen()
    var = tkinter.IntVar()
    label1 = tkinter.Label(app, text="What is your hobby? ", bg="lightblue", font=("David", 20))
    button = tkinter.Button(app, text="next", command=app.destroy, font=("David", 12))
    label1.pack(pady=20)
    button.pack(side="bottom")
    travel_button = tkinter.Radiobutton(app, text="Travel", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=1, font=("David", 14)).pack(anchor=tkinter.CENTER)

    sea_button = tkinter.Radiobutton(app, text="Sea", bg="lightblue", variable=var, pady=5, padx=30,
                                        value=2, font=("David", 14)).pack(anchor=tkinter.CENTER)

    music_button = tkinter.Radiobutton(app, text="Music", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=3, font=("David", 14)).pack(anchor=tkinter.CENTER)
    cook_button = tkinter.Radiobutton(app, text="Cook", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=4, font=("David", 14)).pack(anchor=tkinter.CENTER)
    num = str(var.get())
    if num == "1":
        return "travel"
    elif num == "2":
        return "sea"
    elif num == "3":
        return "music"
    elif num == "4":
        return "cook"
    app.mainloop()


def show_volunteering():
    place_name = get_place.find_place()
    place_info = get_place.return_place_info()
    app = set_screen()
    label1 = tkinter.Label(app, text=f"We found you a volunteering place!\n {place_name}", bg="lightblue", font=("David", 24))
    label1.pack(pady=20)
    label2 = tkinter.Label(app, text=place_info, bg="lightblue", font=("David", 18))
    label2.pack(pady=20)
    app.mainloop()


print("is it working?")
