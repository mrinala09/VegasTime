def main():
    suites = ["club","diamond","heart","spade"]
    suiteChoice = verifyList(suites,"What face (number/royal) would you like your card to be: ")

    numbersNumerical = ["2", "3", "4", "5", "6", "7", "8", "9"]
    numbersWorded = ["two", "three", "four", "five", "six", "seven", "eight", "nine"]
    royals = ["king", "queen", "jack", "ace"]
    faceChoice = verifyList(numbersNumerical+numbersWorded+royals,"What face (number/royal) would you like your card to be: ")

    print(f"{suiteChoice}, {faceChoice}")

def verifyList(list,inputPhrase):
    choice = input(inputPhrase).lower().strip()

    while choice not in list:
        choice = input(inputPhrase).lower().strip()

    return choice

if __name__ == "__main__":
    main()
