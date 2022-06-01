import string


# Fill dictionary with values
def get_bios() -> dict:
    map = {}
    map['BarackObama'] = '44th President of the United States'
    map['SandroPertini'] = 'Former President of the Italian Republic'
    map['NelsonMandela'] = 'Former President of South Africa'
    map['MahatmaGandhi'] = 'Bapu'
    map['DonaldKnuth'] = 'Creator of LaTeX'
    map['DennisRitchie'] = 'Creator of C'
    return map


# Get name from user input
def get_name() -> string:
    return input('Enter a famous name+surname (ex. BarackObama): ')


# Get bio if exist, error otherwise
def get_description(name: string, map: dict) -> string:
    return map[name] if name in map else'Invalid input! Please enter a good name!'


def main() -> None:
    # Create dictionary and fill with values
    bios = get_bios()

    name = get_name()
    # Print bio
    print(get_description(name, bios))


if __name__ == '__main__':
    main()
