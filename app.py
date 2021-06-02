import sys
import configparser
import main_class


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
            mc.update_kv('subject')
            break
        if choice == "n":
            break

    print("Update body?")
    while True:
        choice = input(" (Y)es , (N)o ").lower()
        if choice == "y":
            mc.update_kv()
            break
        if choice == "n":
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
