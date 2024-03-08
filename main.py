def gen_pins():
    # Generates the pins
    pins = {str(n).zfill(4) for n in range(0, 10000)}
    return pins


def save_pins(pins, filename):
    # Saves the pins to a text file
    with open(filename, 'w') as file:
        for pin in pins:
            file.write(f'{pin}\n')


def main():
    # Runs the script, dpoe
    filename = input("Enter the filename for generated PINs: ")
    pins = gen_pins()
    save_pins(pins, filename)
    print(f'Generated: {filename}')


if __name__ == '__main__':
    main()