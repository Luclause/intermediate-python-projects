import curses
import time

menu = ['Home', 'Play', 'Scoreboard', 'Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()

    # Get maximum screen resolution coordinates
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx

        # Highlight selected row item
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)

    # Refresh screen
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0

    print_menu(stdscr, current_row_idx)

    while 1:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu) -1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, f'You pressed {menu[current_row_idx]}')
            stdscr.refresh()
            stdscr.getch()

            # If user selects EXIT, close application
            if current_row_idx == len(menu)-1:
                break

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()

curses.wrapper(main)