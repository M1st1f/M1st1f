#
# user information(working on)
#
emanresu = ("Still")
drowssap = ("a-test")

#
# Title of program
#
print(" ==========∅========= ")
print("   /$$$$$$   /$$$$$$  ")
print("  /$$__  $$ /$$__  $$ ")
print(" | $$  \ $$| $$  \__/ ")
print(" | $$  | $$|  $$$$$$  ")
print(" | $$  | $$ \____  $$ ")
print(" | $$  | $$ /$$  \ $$ ")
print(" |  $$$$$$/|  $$$$$$  ")
print("  \______/  \______/  ")
print(" ==========∅========= ")

#
# start of verifiction
#
print("Please enter your user")

username = input("user: ")
password = input("password: ")

if username == emanresu and password == drowssap:
    print("welcome", username)


print("what you want to do?")
print("1.calculator")
print("2.text writer")
print("3.webbrowser")
print("4.exit")
command = input(">>> ")

#
# Call program calculator.py
#
if command == "1":
    print("========================================================================================")
    print("                     /$$                     /$$             /$$                        ")
    print("                    | $$                    | $$            | $$                        ")
    print("  /$$$$$$$  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ ")
    print(" /$$_____/ |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$")
    print("| $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/")
    print("| $$       /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$      ")
    print("|  $$$$$$$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      ")
    print(" \_______/ \_______/|__/ \_______/ \______/ |__/ \_______/   \___/   \______/ |__/      ")
    print("========================================================================================")
    exec(open("calculator.py").read())
#
# Work in a way to call the program back
#


#
# Working on
#
if command == "2":
    print("==================================================")
    print(" /$$$$$$$  /$$$$$$  /$$$$$$  /$$$$$$$  /$$     /$$")
    print("| $$__  $$|_  $$_/ /$$__  $$| $$__  $$|  $$   /$$/")
    print("| $$  \ $$  | $$  | $$  \ $$| $$  \ $$ \  $$ /$$/ ")
    print("| $$  | $$  | $$  | $$$$$$$$| $$$$$$$/  \  $$$$/  ")
    print("| $$  | $$  | $$  | $$__  $$| $$__  $$   \  $$/   ")
    print("| $$  | $$  | $$  | $$  | $$| $$  \ $$    | $$    ")
    print("| $$$$$$$/ /$$$$$$| $$  | $$| $$  | $$    | $$    ")
    print("|_______/ |______/|__/  |__/|__/  |__/    |__/    ")
    print("==================================================")
    exec(open("text writer.py").read())


if command == "3":
    print("=================================")
    print(" /$$      /$$           /$$      ")
    print("| $$  /$ | $$          | $$      ")
    print("| $$ /$$$| $$  /$$$$$$ | $$$$$$$ ")
    print("| $$/$$ $$ $$ /$$__  $$| $$__  $$")
    print("| $$$$_  $$$$| $$$$$$$$| $$  \ $$")
    print("| $$$/ \  $$$| $$_____/| $$  | $$")
    print("| $$/   \  $$|  $$$$$$$| $$$$$$$/")
    print("|__/     \__/ \_______/|_______/ ")
    print("=================================")
    exec(open("algo interessante.py").read())
#
# program to exit the system
#
if command == "4":
    SystemExit

if command >= "5":
    print("Invalid input")
