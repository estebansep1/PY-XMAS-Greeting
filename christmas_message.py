import time

def print_welcome_message():
    print("🎄🎅🏻 Welcome to annual the Christmas Greeting")

def get_user_name():
    name = input("What's your name? ")
    return name

def print_xmas_greeting(name):
    print("\nHi " + name + "!")
    time.sleep(1)
    print("Wishing you a amagical and joyous Christmas")
    time.sleep(1)
    print("May your days be merry and bright!")
    time.sleep(1)
    print("Merry christmas, " + name + "!")

def main():
    print_welcome_message()
    user_name = get_user_name()
    print_xmas_greeting(user_name)

if __name__ == "__main__":
    main() 