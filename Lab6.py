# Ben Davidson
def encode(password):
    temp_list = [int(i) for i in password]

    for index in range(len(temp_list)):
        if temp_list[index] == 7:
            temp_list[index] = 0
        elif temp_list[index] == 8:
            temp_list[index] = 1
        elif temp_list[index] == 9:
            temp_list[index] = 2
        else:
            temp_list[index] += 3

    temp_list = [str(i) for i in temp_list]
    encoded_password = ''.join(temp_list)

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