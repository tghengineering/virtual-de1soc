import curses

print("Preparing to initialize screen...")
screen = curses.initscr()
print("Screen initialized.")
screen.refresh()

# Update the buffer, adding text at different locations
screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(3, 1, "Try Russian text: Привет")  # Python 3 required for unicode
screen.addstr(3, 4, "X")
screen.addch(5, 5, "Y")

# Changes go in to the screen buffer and only get
# displayed after calling `refresh()` to update
screen.refresh()


curses.napms(2000)
curses.endwin()

print("Window ended.")