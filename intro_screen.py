import tkinter

app = tkinter.Tk()
app.title("Volunteer Quiz")
app.geometry("350x350+500+100")
app.configure(bg="lightblue")
var = tkinter.IntVar()


def introduction_screen():
    intro_label = tkinter.Label(app, text="hello. welcome to Tribu!", bg="lightblue", font=("David", 20))
    intro_label.pack(pady=15)
    next_label = tkinter.Label(app, text="press 'next →' to continue", bg="lightblue", font=("David", 13))
    next_label.pack()

    next_button = tkinter.Button(app, text="next →", command=app.destroy, font=("David", 12))
    next_button.pack(anchor=tkinter.S, padx=10, pady=10, side="bottom")

    app.mainloop()

introduction_screen()