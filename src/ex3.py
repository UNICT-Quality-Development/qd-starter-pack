BIOS = {
    'BarackObama': '44th President of the United States',
    'SandroPertini': 'Former President of the Italian Republic',
    'NelsonMandela': 'Former President of South Africa',
    'MahatmaGandhi': 'Bapu',
    'DonaldKnuth': 'Creator of LaTeX',
    'DennisRitchie': 'Creator of C',
}


# Get name from user input
def get_name() -> str:
    return input('Enter a famous name+surname (ex. BarackObama): ')


# Get bio if exist, error otherwise
def get_description(name: str) -> str:
    return BIOS[name] if name in BIOS else 'Invalid input! Please enter a good name!'


# def main() -> None:
#     name = get_name()
#     # Print bio
#     print(get_description(name, BIOS))


# if __name__ == '__main__':
#     main()
