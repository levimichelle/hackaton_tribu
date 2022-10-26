import tkinter


def selection_hobby(var):
    num = str(var.get())
    if num == "1":
        return "travel"
    elif num == "2":
        return "sea"
    elif num == "3":
        return "music"
    elif num == "4":
        return "cook"


def hobby_screen():
    app = tkinter.Tk()
    app.title("Volunteer Quiz")
    app.geometry("350x350+500+100")
    app.configure(bg="lightblue")
    var = tkinter.IntVar()
    hobby_label = tkinter.Label(app, text="Which of these would you say\nis true about you?", bg="lightblue", font=("David", 20))
    hobby_label.pack(pady=20)

    next_button = tkinter.Button(app, text="next →", command=app.destroy, font=("David", 12))
    next_button.pack(anchor=tkinter.SE, padx=10, pady=10, side="bottom")

    tkinter.Radiobutton(app, text="I enjoy traveling.", bg="lightblue", variable=var, pady=5, padx=30,
                        value=1, font=("David", 14), command=selection_hobby(var)).pack(anchor=tkinter.CENTER)

    tkinter.Radiobutton(app, text="I enjoy being in the sea.", bg="lightblue", variable=var, pady=5, padx=30,
                        value=2, font=("David", 14), command=selection_hobby(var)).pack(anchor=tkinter.CENTER)

    tkinter.Radiobutton(app, text="I enjoy creating music.", bg="lightblue", variable=var, pady=5, padx=30,
                        value=3, font=("David", 14), command=selection_hobby(var)).pack(anchor=tkinter.CENTER)

    tkinter.Radiobutton(app, text="I enjoy cooking.", bg="lightblue", variable=var, pady=5, padx=30,
                        value=4, font=("David", 14), command=selection_hobby(var)).pack(anchor=tkinter.CENTER)

    app.mainloop()
    return selection_hobby(var)

print(hobby_screen())
#
# print(selection_hobby())