myDict = {
    "onePoint":["А", "В", "Е", "И", "Н", "О", "Р", "С", 'Т' ],
    "twoPoints:" :["Д", "К", "Л", "М", "П", "У" ],
    "threePoints:" :["Б", "Г", "Ё", "Ь", "Я"],
    "fourPoints:" :["Ы ", "Й"],
    "fivePoints:" :["Ж", "З", "Х", "Ц", "Ч "],
    "eightPoints:" :["Ш", "Э", "Ю"],
    "tenPoints:" :["Ф", "Щ", "Ъ"],
}

userValue = input("let's start playing, enter a word, to count the score: ")
sumPoints = 0

for item in userValue:
    
    match item:
        case one if item.upper() in myDict["onePoint"]:
            sumPoints += 1
        case two if item.upper() in myDict["twoPoints:"]:
            sumPoints += 2
        case three if item.upper() in myDict["threePoints:"]:
            sumPoints += 3
        case four if item.upper() in myDict["fourPoints:"]:
            sumPoints += 4
        case five if item.upper() in myDict["fivePoints:"]:
            sumPoints +=5
        case eight if item.upper() in myDict["eightPoints:"]:
            sumPoints += 8
        case ten if item.upper() in myDict["tenPoints:"]:
            sumPoints += 10
        case _:
            sumPoints = 0

    # if item in myDict["onePoint"]: 
    #     sumPoints += 1
    #     print("one point")
    # elif item in myDict["twoPoints:"]:
    #     sumPoints +=2
    #     print("2 point")
    # elif item in myDict["fivePoints:"]:
    #     sumPoints +=5
    #     print("5 point")

print(f"The Total score is: {sumPoints}")

if sumPoints == 0: 
    print("May be you enterd some wrong characters")




