__author__ = 'Glenn'
import sys

from pip._vendor.distlib.compat import raw_input

from library import get_ipadresses, network_sniffer
from Glenn import connect_socket_test
from Bob import menu_Bob


c = "+"
h = "-"

while True:
    print(c + h*78 + c)
    print ("""\
                                                    .=I
                                                    O$::
                                                    II8O
                  M                                ID?
                  M         +                   M???I++
                  =        MIMI:M.M             IM7$ID+?
                  M        7     7I              ZID?I8$M
                 I$.      ?        M~=+MM~7M     MZ$I7$M
                 +I?     ~        I=7 +O7  MM     $??7
                   I++M?:M        7??+O?7.  I    :=
               .??7$7??Z?          ZM=Z$.    ?  ,M
               $7I7$$$?Z?         M?Z~ZO,    ?,7
                M77DM77M          +O$=Z8O     M
                  $7Z$           D~.  +$7
                    ,Z          ?I?+=~7ZOO,
                    MO      MMMMZ$+++I+M??$MMM7
                             88:M=:MM,+MM?M~M8D
                             .MI~=::~:?++?MNMM
                               M7=::~:?=~?MM
                  II             =::~:?=~?M                  $?.  I
                  MII            =::~?~~=?M                 ,       =
                   O77           +~::~::=I                 N
                   MOM          MM=~MMM~?:O                M         .
                 D7?$I   . MMMM??M=~~~~=IM$OZMM= ~          M       .
               .7II$ZIIO7DOOMI?I?,==:,~?M=IZ7OM88MZM        .M     M
               7$OZOMZMO?+??Z?+?7. ==~=M==I$7$M7$ZZZ$          ~IM
               M$$M88$Z$????M?+?7M  M?,  ,?$7$OI77ZZ$.     MI7OIII$
                MZ$$8O$IMI??I$M?7ZMM=ZM=O7+7Z$7I7ZZ$$$M    M$7MZZZ7
                M,+M+?MIMI???OI??I$,,$O,7+77ZOMI7ZM$7M     M$M87I78
               M+MMMMNZMMII???IO7I?I7M?=?7$ZOZZI$Z=$=$      MMMMD$
               MMMII+Z=7M77I????IZI?+I$ZZMMZZ??7ZO=$7~      .OMOO7
               .?MII7$ZMOM$77I7I??ZZZZOOOOO???I$ZOM$I:      MO887
               .?:?II$ZMOIIZMO7I.M++++++??=~OOMMM$O7?IM +7N8=O.
                ?$$+I$ZMM8I??N77$M?+++++??MZZ$OOZ+M7?M??$MM=$M
               M+==+I$ZMOMI?IZ77II???++??II7$ZZOZM7M??I?$8$ZM8M
               M+=+?7ZOOOM7IIZ$77III????II7$ZZZZZO$7III7$=MNNM.
               ,I?I7ZZOOM 77IZ$$777IIIIII77$ZZZZ=OO$$$MZZZZZOM
                M$ZZOOM   M$$$$$$$777777777$$$$$$MOOZZ+IZ$M
                             $M$$$$$$777$$$$$$$$   M=+M

    o   o      o                     o               o-o         o           o
    |\  |      |                     |              o            |           |
    | \ | o-o -o- o-o o-o  o-o  o-o -o- o-o o-o     |  -o  oo  o-O o--o o-o -o-
    |  \| |-'  |   \  |  | |-' |     |  | | |       o   | | | |  | |  | |-'  |
    o   o o-o  o  o-o O-o  o-o  o-o  o  o-o o        o-o  o-o- o-o o--O o-o  o
                      |                                               |
                      o                                            o--o
                  """)
    print(c + h*78 + c)
    print()
    print(" "*28 + "1: Toon IP adressen")
    print(" "*28 + "2: Test Socket connectie")
    print(" "*28 + "3: Simple Network sniffer")
    print(" "*28 + "4: ")
    print(" "*28 + "5: Menu Bob")
    print(" "*28 + "0: Afsluiten")
    print()
    input = optie_input = raw_input(" "*28 + "Kies een optie: ",)
    print(optie_input)
    print(c + h*78 + c)
    if optie_input == '1':
        print(get_ipadresses.show_ipadresses())
    elif optie_input == '2':
        print(connect_socket_test.connect_socket())
    elif optie_input == '3':
        print(network_sniffer.sniffer())
    elif optie_input == '5':
        print(menu_Bob.menu_bob())
    elif optie_input == '0':
        sys.exit(0)