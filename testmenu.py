#!/usr/bin/env python
import sys
import curses
from pip._vendor.distlib.compat import raw_input

from library import get_ipadresses, network_sniffer
from Glenn import connect_socket_test
from Bob import menu_Bob
from Glenn import act_on_input


screen = curses.initscr()

curses.start_color()
# curses.init_pair(1, curses.COLOR_BLUE,)

c = "+"
h = "-"

screen.clear()
screen.border(0)
screen.addstr(1, 1, c + h * 80 + c)
screen.addstr(2, 1, """|      __     _                       _                                          |""")
screen.addstr(3, 1, """|   /\ \ \___| |_ ___ _ __   ___  ___| |_ ___  _ __                              |""")
screen.addstr(4, 1, """|  /  \/ / _ \ __/ __| '_ \ / _ \/ __| __/ _ \| '__|                             |""")
screen.addstr(5, 1, """| / /\  /  __/ |_\__ \ |_) |  __/ (__| || (_) | |                                |""")
screen.addstr(6, 1, """| \_\ \/ \___|\__|___/ .__/ \___|\___|\__\___/|_|                                |""")
screen.addstr(7, 1, """|                    |_|                                                         |""")
screen.addstr(8, 1, """|    ___          _            _                                                 |""")
screen.addstr(9, 1, """|   / _ \__ _  __| | __ _  ___| |_                                               |""")
screen.addstr(10, 1, """|  / /_\/ _` |/ _` |/ _` |/ _ \ __|                                              |""")
screen.addstr(11, 1, """| / /_\\\ (_| | (_| | (_| |  __/ |_                                               |""")
screen.addstr(12, 1, """| \____/\__,_|\__,_|\__, |\___|\__|                                              |""")
screen.addstr(13, 1, """|                   |___/                                                        |""")
screen.addstr(14, 1, c + h * 80 + c)

screen.addstr(16, 1, "1: Toon IP adressen")
screen.addstr(17, 1, "2: Test Socket connectie")
screen.addstr(18, 1, "3: Simple Network sniffer")
screen.addstr(19, 1, "4: ")
screen.addstr(20, 1, "5: Menu Bob")
screen.addstr(21, 1, "0: Afsluiten")
screen.refresh()

act_on_input(screen, {ESC: quit,
                             "1": live,
                             "2": history,
                             "3": connect,
                             "4": agent,
                             "5": bunny})




# screen.addstr(25, 1, optie_input)
# if optie_input == '1':
#    print(get_ipadresses.show_ipadresses())
#elif optie_input == '2':
#    print(connect_socket_test.connect_socket())
#elif optie_input == '3':
#    print(network_sniffer.sniffer())
#elif optie_input == '5':
#    print(menu_Bob.menu_bob())
#elif optie_input == '0':
#    sys.exit(0)

#screen.refresh()
#opt = screen.getch()
#curses.endwin()