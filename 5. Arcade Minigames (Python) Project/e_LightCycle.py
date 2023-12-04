import turtle
from supporting_LightCycle_helper import Vector
import sys
import time

def choose_option(filename):
    """
    1) Takes in a text file's name as a string (e.g. "settings.txt")
        - First line in text file should contain dialogue to be displayed
        - Subsequent lines should contain the list of options, with one line for each option
        - Each option should have a Displayed value followed by an Actual value. Both are to be
        seperated by a comma (,)

    2) Prompts user for input with a dialogue consisting of first line in text file + each option's
    Displayed value and the corresponding input to select it. 

    3) Repeats step 2 until a valid input is received

    4) Returns the Actual value of the option corresponding to selected input
    """
    options, dialogue2 = [], ""
    # read file, generate dialogue
    with open(filename, "r") as f:
        dialogue1 = f.readline().strip()
        for index, line in enumerate(f):
            opt = line.split(",")
            options.append(opt)
            dialogue2 += f"\n'{index+1}' for {opt[0]}"
        f.close()

    selected_opt = 0
    # prompts user for input until a valid input is received
    while selected_opt == 0:
        selection = input(f"\n{dialogue1} {dialogue2}\n")
        if 0 < int(selection) <= len(options):
            selected_opt = options[int(selection)-1][1]
        else:
            print("Invalid input!\n")

    return int(selected_opt)

def draw_square(size, colour, x_offset, y_offset, fill=True):
    """
    1) Takes in the following arguments:
        - integer 'size': length of square's sides
        - string 'colour': colour of square's outline and/or fill
        - integer 'x_offset': x position of square 
        - integer 'y_offset': y position of square 
        - boolean 'fill': whether to fill square with colour (defaults to True if not passed in)

    2) Draws square on screen using arguments passed in
    """
    t.up()
    t.goto(x_offset, y_offset)
    t.down()
    t.color(colour)
    if fill:
        t.begin_fill()

    for _ in range(4):
        t.forward(size)
        t.right(90)

    if fill:
        t.end_fill()

def in_boundary(head, res):
    """
    1) Takes in a vector object 'head' and an integer 'res'

    2) Specifies x and y boundaries using the res value passed in

    3) Return True if 'head' is within the specified boundaries
    """
    min_x_bound, min_y_bound = -res/2 + res*0.015, -res/2 + res*0.035
    max_x_bound, max_y_bound = res/2 - res*0.035, res/2 - res*0.02
    return min_x_bound < head.x < max_x_bound and min_y_bound < head.y < max_y_bound

def render():
    """Represents a single 'frame' of the game
    """

    # FOR DEBUGGING
    # global framecount
    # framecount+=1
    # print(framecount)

    # move players by 1 step
    p1_pos.translate(p1_dir)
    p1_head = p1_pos.copy()
    p2_pos.translate(p2_dir)
    p2_head = p2_pos.copy()

    # check for game over conditions
    if not in_boundary(p1_head, res) or p1_head in p2_trail or p1_head in p1_trail:
        print('\nOrange won! Press Escape to exit.')
        return
    if not in_boundary(p2_head, res) or p2_head in p1_trail or p2_head in p2_trail:
        print('\nCyan won! Press Escape to exit.')
        return

    # add current position to trail
    p1_trail.add(p1_head)
    p2_trail.add(p2_head)

    # draw squares
    draw_square(res/200, "cyan", p1_pos.x, p1_pos.y)
    draw_square(res/200, "orange", p2_pos.x, p2_pos.y)
    s.update()

    # proceed to next frame after 'diff' milliseconds
    s.ontimer(render, diff)

def main():
    """Call this to start the game
    """
    global framecount, s, t, res, diff, p1_pos, p2_pos, p1_dir, p2_dir, p1_trail, p2_trail
    
    # FOR DEBUGGING
    # framecount = 0

    # print welcome dialogue
    with open("supporting_file_welcome.txt", "r") as f:
        for index, line in enumerate(f):
            print(line.strip("\n"))
        f.close()

    # prompt user to specify options
    res = choose_option("supporting_file_resolutions.txt")
    diff = choose_option("supporting_file_difficulties.txt")

    print("")

    # countdown to game start
    sys.stdout.write("Game starts in 3 seconds")
    backspace = "\b"*9
    for i in range(2, 0, -1):
        sys.stdout.write(f"{backspace}{i} seconds")
        sys.stdout.flush()
        time.sleep(1)
    print("\nGame started!")

    # instantiate starting vectors
    p1_pos = Vector(-10, -res/3)
    p2_pos = Vector(-10, res/3)
    p1_dir = Vector(0, 4)
    p2_dir = Vector(0, -4)
    p1_trail = set()
    p2_trail = set()

    # setup turtle
    turtle.TurtleScreen._RUNNING = True
    s, t = turtle.Screen(), turtle.Turtle()
    s.setup(res, res, 360, 0)
    s.bgcolor("black")
    t.hideturtle()
    s.tracer(False)
    draw_square(res-res*0.05, "orange", -(res/2)+res*0.02, (res/2)-res*0.02, False)
    s.listen()

    # define controls
    s.onkey(lambda: p1_dir.rotate("up"), 'w')
    s.onkey(lambda: p1_dir.rotate("left"), 'a')
    s.onkey(lambda: p1_dir.rotate("down"), 's')
    s.onkey(lambda: p1_dir.rotate("right"), 'd')

    s.onkey(lambda: p2_dir.rotate("up"), 'Up')
    s.onkey(lambda: p2_dir.rotate("left"), 'Left')
    s.onkey(lambda: p2_dir.rotate("down"), 'Down')
    s.onkey(lambda: p2_dir.rotate("right"), 'Right')

    render()
    s.onkey(s.bye, 'Escape')
    s.mainloop()

# main()
