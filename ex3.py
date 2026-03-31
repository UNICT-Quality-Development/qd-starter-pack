#Python version of the "Famous Person" program (Using "match")
famous_person = input("Enter a famous name + surname, e.g. Barack Obama: ")

match famous_person:
    case "Barack Obama":
        print("44th president of the United States")
    case "Sandro Pertini":
        print("Former President of the Italian Republic")
    case "Nelson Mandela":
        print("Former President of South Africa")
    case "Mahatma Gandhi":
        print("Bapu")
    case "Donald Knuth":
        print("Creator of LaTeX")
    case "Dennis Ritchie":
        print("Creator of C")
    case _:
        print("Invalid input! Please enter a good name!")
#Using the same format of each case, it's possible to freely add more famous people to the list