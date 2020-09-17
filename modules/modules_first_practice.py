from tkinter import *
from PIL import Image, ImageTk


def show_pick():
    load = Image.open("img_6.1_3_2.png")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=50)


def question_window():
    """
    creates a gui, window and button that opens a picture
    """
    # Tk() initialize the window manager and assign it to a variable.
    window = Tk()
    window.geometry("436x237")
    # rename the title of the window
    window.title("question")
    #  insert some text into the window.
    my_label = Label(window, text="who is the professor?")
    # display the widget in size it requires.
    my_label.pack()
    # initialize a button
    my_button = Button(window, text="click to find out",
                       command=show_pick)
    my_button.pack()
    # display the window until manually close. runs an infinite loop.
    window.mainloop()


if __name__ == '__main__':
    question_window()