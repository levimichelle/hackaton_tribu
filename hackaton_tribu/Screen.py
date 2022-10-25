import tkinter
# from tkinter import messagebox

def set_screen():
    app = tkinter.Tk()
    app.title("Volunteer Quiz")
    app.geometry("350x350+500+100")
    app.configure(bg="lightblue")
    return app

def introduction_screen():
    pass


def place_screen():
    app = set_screen()
    var = tkinter.IntVar()
    label1 = tkinter.Label(app, text="What region are you from?", bg="lightblue", font=("David", 20))
    label1.pack(pady=20)

    north_button = tkinter.Radiobutton(app, text="north", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=1, font=("David", 14)).pack(anchor=tkinter.CENTER)

    center_button = tkinter.Radiobutton(app, text="center", bg="lightblue", variable=var, pady=5, padx=30,
                                        value=2, font=("David", 14)).pack(anchor=tkinter.CENTER)

    south_button = tkinter.Radiobutton(app, text="south", bg="lightblue", variable=var, pady=5, padx=30,
                                       value=3, font=("David", 14)).pack(anchor=tkinter.CENTER)

    app.mainloop()

place_screen()
