import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table lang (name, first_appeared)")
# This is the qmark style:
cur.execute("insert into lang values (?, ?)", ("C", 1972))
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]
cur.executemany("insert into lang values (?, ?)", lang_list)

for row in cur.execute("select * from lang where first_appeared=:year", {"year": 1972}):
    print(str(row[0]) + ' - ' + str(row[1]))
con.close()
# ----------------------------------------------------------------------------

from colorama import init, Fore, Back, Style


# essential for Windows environment
init()
FORES = [ Fore.RED, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

def print_with_color(s, color=Fore.WHITE, brightness=Style.BRIGHT, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)

# printing all available foreground colors with different brightness
for fore in FORES:
    print_with_color("Hello world!", color=fore)

print_with_color('hi ekim', Fore.GREEN)
