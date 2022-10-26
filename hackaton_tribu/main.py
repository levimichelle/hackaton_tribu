import tkinter

import consts
import Screen
import get_place

def main():
    Screen.introduction_screen()
    Screen.region_screen()
    Screen.hobby_screen()
    Screen.show_volunteering()


if __name__ == '__main__':
    main()


def get_user_event():
    tkinter.EventType