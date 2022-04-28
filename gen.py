import random
import string

length = int(input(
"""
██╗     ███████╗███╗   ██╗ ██████╗████████╗██╗  ██╗    ██████╗ 
██║     ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║  ██║    ╚════██╗
██║     █████╗  ██╔██╗ ██║██║  ███╗  ██║   ███████║      ▄███╔╝
██║     ██╔══╝  ██║╚██╗██║██║   ██║  ██║   ██╔══██║      ▀▀══╝ 
███████╗███████╗██║ ╚████║╚██████╔╝  ██║   ██║  ██║      ██╗   
╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝\n\n"""))

name = input("""
███╗   ██╗ █████╗ ███╗   ███╗███████╗    ██████╗ 
████╗  ██║██╔══██╗████╗ ████║██╔════╝    ╚════██╗
██╔██╗ ██║███████║██╔████╔██║█████╗        ▄███╔╝
██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝        ▀▀══╝ 
██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗      ██╗   
╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝      ╚═╝\n\n""")

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)

password = "".join(temp)

open('secrets.txt', 'a').write(f"\nName: {name} \n\nPassword: {password}")
print(f"\nName: {name} \n\nPassword: {password}")

