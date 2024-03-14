# Ben Davidson

def encode(password):
    temp_list = [int(i) + 3 for i in password]
    temp_list = [str(i) for i in temp_list]
    encoded_password = "".join(temp_list)

    return encoded_password


def decode(password):
    pass


def main():
    while True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        menu_choice = int(input("Please enter an option: "))

        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif menu_choice == 2:
            pass
        else:
            break


if __name__ == '__main__':
    main()