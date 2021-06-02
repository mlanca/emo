import sys
import main_class
import configparser


def main():
    config = configparser.RawConfigParser()
    config.read('env.ini')
    db_name = config["DEFAULT"]["DATABASE"]
    mc = main_class.main_class(db_name)
    mc.list_clients()
    print("Welcome ...")
    while True:
        choice = input(" (Y)es , (N)o, (Q)uit ").lower()
        if choice == "y":
            mc.add_client()
            mc.list_clients()
        if choice == "n":
            break
        if choice == "q":
            sys.exit("Bye...")
    print("Update subject?")
    while True:
        choice = input(" (Y)es , (N)o ").lower()
        if choice == "y":
            mc.update_subject()
            break
        elif choice == "n":
            break

    print("Update body?")
    while True:
        choice = input(" (Y)es , (N)o ").lower()

        if choice == "y":
            mc.update_body()
            break
        elif choice == "n":
            break
    print("Send email?")
    while True:
        choice = input(" (Y)es , (N)o ").lower()
        if choice == "y":
            mc.send_email()
            break
        elif choice == "n":
            sys.exit("Bye...")


if __name__ == "__main__":
    main()
