import a_TicTacToe, b_Hangman, c_RockPaperScissors, d_Blackjack, e_LightCycle, f_SpaceInvaders

def choose_option(filename):
    """
    1) Takes in a text file's name as a string (e.g. "settings.txt")
        - First line in text file should contain dialogue to be displayed
        - Subsequent lines should contain the list of options, with one line for each option
        - Each option should have a Displayed value followed by an Actual value. Both are to be
        seperated by the character "|"

    2) Prompts user for input with a dialogue consisting of first line in text file + each option's
    Displayed value and the corresponding input to select it. 

    3) Repeats step 2 until a valid input is received

    4) Executes the Actual value of the option corresponding to selected input
    """
    options, dialogue2 = [], ""
    # read file, generate dialogue
    with open(filename, "r") as f:
        dialogue1 = f.readline().strip()
        for index, line in enumerate(f):
            opt = line.split("|")
            options.append(opt)
            dialogue2 += f"\n'{index+1}' for {opt[0]}"
        f.close()

    selected_opt = 0
    # prompts user for input until a valid input is received
    while selected_opt == 0:
        selection = input(f"\n{dialogue1} {dialogue2}\n")
        if selection.upper() == "EXIT":
            return
        elif 0 < int(selection) <= len(options):
            selected_opt = options[int(selection)-1][1]
        else:
            print("Invalid input!\n")

    print("")
    exec(selected_opt)
    choose_option("supporting_file_gamelist.txt")

choose_option("supporting_file_gamelist.txt")
