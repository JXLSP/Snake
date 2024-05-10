import curses
from curses import wrapper


def main(stdscr):
    height, width = stdscr.getmaxyx()
    text = "战神Snake"
    text_width = len(text)

    start = (width // 2) - (text_width // 2)

    stdscr.addstr(height // 2, start, text)
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()


wrapper(main)


