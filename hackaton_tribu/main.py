import tkinter
import volunteer_screen
import intro_screen
import region_screen
import hobby_screen


def main():
    intro_screen.introduction_screen()
    # region_screen.region_screen()
    # volunteer_screen.show_volunteering()


if __name__ == '__main__':
    main()


def get_user_event():
    tkinter.EventType