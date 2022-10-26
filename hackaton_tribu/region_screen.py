import tkinter


def selection_place(var):
    num = str(var.get())
    if num == "1":
        return "north"
    elif num == "2":
        return "center"
    elif num == "3":
        return "south"


def region_screen():
    app = tkinter.Tk()
    app.title("Volunteer Quiz")
    app.geometry("350x350+500+100")
    app.configure(bg="lightblue")
    var = tkinter.IntVar()
    region_label = tkinter.Label(app, text="What region are you from?", bg="lightblue", font=("David", 20))
    region_label.pack(pady=20)

    next_button = tkinter.Button(app, text="next →", command=app.destroy, font=("David", 12))
    next_button.pack(anchor=tkinter.SE, padx=10, pady=10, side="bottom")

    tkinter.Radiobutton(app, text="north", bg="lightblue", variable=var, pady=5, padx=30,
                        value=1, font=("David", 14), command=selection_place(var)).pack(anchor=tkinter.CENTER)

    tkinter.Radiobutton(app, text="center", bg="lightblue", variable=var, pady=5, padx=30,
                        value=2, font=("David", 14), command=selection_place(var)).pack(anchor=tkinter.CENTER)

    tkinter.Radiobutton(app, text="south", bg="lightblue", variable=var, pady=5, padx=30,
                        value=3, font=("David", 14), command=selection_place(var)).pack(anchor=tkinter.CENTER)

    app.mainloop()
    return selection_place(var)

#
# print(region_screen())
