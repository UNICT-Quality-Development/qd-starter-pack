from src.ex3 import who_is

dictionary = {"BarackObama":"44th president of the United States",
                  "SandroPertini":"Former President of the Italian Republic",
                  "NelsonMandela":"Former President of South Africa",
                  "MahatmaGandhi":"Bapu",
                  "DonaldKnuth":"Creator of LaTeX",
                  "DennisRitchie":"Creator of C"}

def test_day_of_week() -> None:
    assert who_is("BarackObama",dictionary) == "44th president of the United States"
    assert who_is("SandroPertini",dictionary) == "Former President of the Italian Republic"
    assert who_is("NelsonMandela",dictionary) == "Former President of South Africa"
    assert who_is("MahatmaGandhi",dictionary) == "Bapu"
    assert who_is("DonaldKnuth",dictionary) == "Creator of LaTeX"
    assert who_is("DennisRitchie",dictionary) == "Creator of C"
    assert who_is("ABCDEFG",dictionary) == "Invalid input! Please enter a good name!"
    