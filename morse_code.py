import pyautogui as pag

choose = pag.confirm(text='Convert to:', title='Morse Code Translator', buttons=['Morse code', 'Text'])

if choose == "Morse code":
    input_text_1 = pag.prompt(text='Enter your text:', title='Text To Morse Code', default='')
    convert_1 = list(input_text_1)
    for x in convert_1:
        if x.lower() == "a":
            print("•-", end=" ")

        if x.lower() == "b":
            print("-•••", end=" ")

        if x.lower() == "c":
            print("-•-•", end=" ")

        if x.lower() == "d":
            print("-••", end=" ")

        if x.lower() == "e":
            print("•", end=" ")

        if x.lower() == "f":
            print("••-•", end=" ")

        if x.lower() == "g":
            print("--•", end=" ")

        if x.lower() == "h":
            print("••••", end=" ")

        if x.lower() == "i":
            print("••", end=" ")

        if x.lower() == "j":
            print("•---", end=" ")

        if x.lower() == "k":
            print("-•-", end=" ")

        if x.lower() == "l":
            print("•-••", end=" ")

        if x.lower() == "m":
            print("--", end=" ")

        if x.lower() == "n":
            print("-•", end=" ")

        if x.lower() == "o":
            print("---", end=" ")

        if x.lower() == "p":
            print("•--•", end=" ")

        if x.lower() == "q":
            print("--•-", end=" ")

        if x.lower() == "r":
            print("•-•", end=" ")

        if x.lower() == "s":
            print("•••", end=" ")

        if x.lower() == "t":
            print("-", end=" ")

        if x.lower() == "u":
            print("••-", end=" ")

        if x.lower() == "v":
            print("•••-", end=" ")

        if x.lower() == "w":
            print("•--", end=" ")

        if x.lower() == "x":
            print("-••-", end=" ")

        if x.lower() == "y":
            print("-•--", end=" ")

        if x.lower() == "z":
            print("--••", end=" ")

        if x == "1":
            print("•----", end=" ")

        if x == "2":
            print("••---", end=" ")

        if x == "3":
            print("•••--", end=" ")

        if x == "4":
            print("••••-", end=" ")

        if x == "5":
            print("•••••", end=" ")

        if x == "6":
            print("-••••", end=" ")

        if x == "7":
            print("--•••", end=" ")

        if x == "8":
            print("---••", end=" ")

        if x == "9":
            print("----•", end=" ")

        if x == "0":
            print("-----", end=" ")

        if x == ".":
            print("•-•-•-", end=" ")

        if x == ",":
            print("--••--", end=" ")

        if x == "?":
            print("••--••", end=" ")

        if x == " ":
            print("_", end=" ")


elif choose == "Text":
    input_text_2 = pag.prompt(text='Enter your text:', title='Morse Code To Text', default='')
    convert_2 = input_text_2.split()
    for x in convert_2:
        if x == "•-":
            print("a", end="")

        if x == "-•••":
            print("b", end="")

        if x == "-•-•":
            print("c", end="")

        if x == "-••":
            print("d", end="")

        if x == "•":
            print("e", end="")

        if x == "••-•":
            print("f", end="")

        if x == "--•":
            print("g", end="")

        if x == "••••":
            print("h", end="")

        if x == "••":
            print("i", end="")

        if x == "•---":
            print("j", end="")

        if x == "-•-":
            print("k", end="")

        if x == "•-••":
            print("l", end="")

        if x == "--":
            print("m", end="")

        if x == "-•":
            print("n", end="")

        if x == "---":
            print("o", end="")

        if x == "•--•":
            print("p", end="")

        if x == "--•-":
            print("q", end="")

        if x == "•-•":
            print("r", end="")

        if x == "•••":
            print("s", end="")

        if x == "-":
            print("t", end="")

        if x == "••-":
            print("u", end="")

        if x == "•••-":
            print("v", end="")

        if x == "•--":
            print("w", end="")

        if x == "-••-":
            print("x", end="")

        if x == "-•--":
            print("y", end="")

        if x == "--••":
            print("z", end="")

        if x == "•----":
            print("1", end="")

        if x == "••---":
            print("2", end="")

        if x == "•••--":
            print("3", end="")

        if x == "••••-":
            print("4", end="")

        if x == "•••••":
            print("5", end="")

        if x == "-••••":
            print("6", end="")

        if x == "--•••":
            print("7", end="")

        if x == "---••":
            print("8", end="")

        if x == "----•":
            print("9", end="")

        if x == "-----":
            print("0", end="")

        if x == "•-•-•-":
            print(".", end="")

        if x == "--••--":
            print(",", end="")

        if x == "••--••":
            print("?", end="")

        if x == "_":
            print(" ", end="")
else:
    pass
