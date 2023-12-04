import tkinter as tk
import random



# How the coordinate system in tkinter works:
# To form an object, tkinter needs x1, x2, y1, y2 coordinates.
# x1, y1 being the top left of the object
# x2, y2 being the bottom right of an object
# tkinter will connect the dots to form the shape that you want.
# Height of canvas is created from top-down (top is 0)
# Width of canvas is created from left-right (left is 0)

# Player class
class Player:
    def __init__(self, canvas, master, x, y, name, lives):  # Where x and y are the coordinates of the object.
        self.speed_x = 0  # How fast the object will move in the x-direction.
        self.speed_y = 0  # How fast the object will move in the y-direction.
        self.lives = lives
        self.name = name
        self.master = master
        self.label = canvas.create_text(x, y - 30, text=f"{self.name} Lives: {self.lives}", fill="white")
        self.canvas = canvas
        self.score = 0
        self.player = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='purple')
        self.score_label = canvas.create_text(x - 255, y - 540, text=f"Score: {self.score}", fill="white")

    # Movements - left, right, up, down.
    # Calls the move() method everytime an arrow key is pressed.
    # The move() method prevents the Player object to go beyond the boundaries of the canvas.
    # Self.speed_x and self.speed_y determines how much (in units) the objects move.
    # Self.speed_x = 10 means the object is moving 10 speed to the right (Right as positive)
    # Self.speed_y = -10 means the object will move 10 units up (Downwards as positive)
    def move_left(self, event):
        self.speed_x = -20
        self.speed_y = 0
        self.move()

    def move_right(self, event):
        self.speed_x = 20
        self.speed_y = 0
        self.move()

    def move_up(self, event):
        self.speed_y = -20
        self.speed_x = 0
        self.move()

    def move_down(self, event):
        self.speed_y = 20
        self.speed_x = 0
        self.move()

    # Gets the 4 coordinates (x1, y1, x2, y2) of the object.
    def get_position(self):
        return self.canvas.coords(self.player)

    # Method to check if the Player object exceeds the boundaries of the canvas.
    def move(self):
        # Moves by how much it was specified in the methods above.
        self.canvas.move(self.label, self.speed_x, self.speed_y)
        self.canvas.move(self.player, self.speed_x, self.speed_y)

        coords = self.canvas.coords(self.player)  # Gets the coordinates of the object.
        width = self.canvas.winfo_width()  # Gets the width of the canvas (600).
        height = self.canvas.winfo_height()  # Gets the height of the canvas (600).

        if coords[0] < 0:  # x1 coordinate of the object is smaller than 0 (Left of the canvas).
            self.canvas.move(self.label, -coords[0], 0)  # Moves in the opposite direction by how much it exceeds the left boundary.
            self.canvas.move(self.player, -coords[0], 0)  # Moves in the opposite direction by how much it exceeds the left boundary.

        elif coords[2] > width:  # x2 coordinate of the object is bigger than 600 (Right of the canvas).
            self.canvas.move(self.label, width - coords[2], 0)  # Moves in the opposite direction by how much it exceeds the right boundary.
            self.canvas.move(self.player, width - coords[2], 0)  # Moves in the opposite direction by how much it exceeds the right boundary.

        if coords[1] < 0:  # y1 coordinate of the object is smaller than 0 (Top of the canvas).
            self.canvas.move(self.label, 0, -coords[1])  # Moves in the opposite direction by how much it exceeds the top boundary.
            self.canvas.move(self.player, 0, -coords[1])  # Moves in the opposite direction by how much it exceeds the top boundary.

        elif coords[3] > height:  # y2 coordinate of the object is bigger than 600 (Bottom of the canvas).
            self.canvas.move(self.label, 0, height - coords[3])  # Moves in the opposite direction by how much it exceeds the bottom boundary.
            self.canvas.move(self.player, 0, height - coords[3])  # Moves in the opposite direction by how much it exceeds the bottom boundary.

    # Method to decrease lives of player.
    def decrease_lives(self):
        self.lives -= 1
        if self.lives >= 0:
            self.canvas.itemconfig(self.label, text=f"{self.name} Lives: {self.lives}")  # To modify the parameters of the tkinter object.
        if self.lives == 0:
            self.show_game_over()
            print("Game over")

    def update_score_label(self):
        self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")

    def show_game_over(self):
        game_over_label = tk.Label(self.canvas, text=f"Game Over\nFinal Score: {self.score}", font=("Helvetica", 24), fg="red")
        self.canvas.create_window(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, window=game_over_label)
        self.master.after(2000, self.master.destroy)  # Close the window after 2 seconds (2000 milliseconds).

# Monster class
class Monster:
    def __init__(self, canvas, no_of_monsters, canvas_width, canvas_height):
        self.canvas = canvas
        self.enemies = []  # Array of enemies.

        # Creating the enemies.
        for i in range(no_of_monsters):
            enemy = self.generate_enemy(canvas_width, canvas_height)  # Calls the generate_enemy method for each iteration for some condition checks.
            self.enemies.append(enemy)  # Adds each enemy into the self.enemies list.

    # Checks if the newly generated enemies overlaps each other.
    # If overlaps, don't generate.
    # If no overlaps, spawn the new enemies.
    def generate_enemy(self, canvas_width, canvas_height):  # Takes in the height and width of canvas to ensure enemies spawn
        while True:
            # Coordinates of new enemies:
            x1 = random.randint(0, canvas_width - 20)  # Ensures starting point of each enemy is different and random.
            y1 = canvas_height  # Ensures the enemies always spawn at the top of the canvas. That's why canvas_height is always set to 0 when an instance of the object is initialized.
            x2 = x1 + 30
            y2 = y1 + 20

            # Check for overlap with existing enemies
            overlap = False  # Set overlap to false so new enemies will always spawn by default.
            for existing_enemy in self.enemies:  # Check against the list of existing of enemies
                ex1, ey1, ex2, ey2 = self.canvas.coords(existing_enemy)  # Get coordinates of existing enemies.
                if (x1 < ex2 and x2 > ex1) and (y1 < ey2 and y2 > ey1):  # If the new enemies' x and y coordinates is in between the existing enemies, set overlap True.
                    overlap = True
                    break  # Breaks the loop

            if not overlap:  # If overlap is False, generate new enemies.
                color = random.choice(['red', 'blue', 'yellow'])  # Probably can do something with the colors. For now, the different colors mean nothing.
                enemy = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)  # Create new instance of the object (I.e., the enemy).
                return enemy

    # Movement of the enemy from top to bottom.
    def move(self, red_line, lives, timer):
        for enemy in self.enemies:
            if timer > 15:
                self.canvas.move(enemy, 0, 4)
            elif timer > 30:
                self.canvas.move(enemy, 0, 5)
            elif timer > 45:
                self.canvas.move(enemy, 0, 6)
            elif timer > 45:
                self.canvas.move(enemy, 0, 7)
            else:
                self.canvas.move(enemy, 0, 2.5)  # Probably should add more features. If the players survive for a certain period of time, can probably increase the speed of the enemies.
        for enemy in self.enemies[:]:  # Creates a shallow copy of the list to prevent unexpected behaviours because length of list is changing dynamically.
            enemy_coords = self.canvas.coords(enemy)
            if enemy_coords[3] > red_line:  # If enemies exceed the red line, delete and remove from list.
                self.canvas.delete(enemy)
                self.enemies.remove(enemy)
                lives.decrease_lives()


# Projectile class
class Projectile:
    def __init__(self, canvas, x, y, player):
        self.canvas = canvas
        self.player = player
        self.projectile = canvas.create_oval(x + 10, y + 10, x, y, fill='green')

    def move(self, enemies):
        self.canvas.move(self.projectile, 0, -25)  # Speed of the projectile.
        coords = self.canvas.coords(self.projectile)

        # If projectile exceed the top boundary, delete. Else, call the self.check_collision() method.
        if coords:
            if coords[1] < 0:
                self.canvas.delete(self.projectile)
            else:
                self.check_collision(enemies, self.player)  # Check for collision with the enemies.

    # Method to check for collision.
    def check_collision(self, enemies, player):
        projectile_coords = self.canvas.coords(self.projectile)

        #  If projectile hits the enemies, delete the projectile and the enemy and remove the enemies from the list.
        for enemy in enemies:
            enemy_coords = self.canvas.coords(enemy)
            if self.is_collision(projectile_coords, enemy_coords):  # Collision between projectile and enemies is true:
                self.canvas.delete(self.projectile)
                self.canvas.delete(enemy)
                enemies.remove(enemy)
                player.score += 10
                player.update_score_label()

    @staticmethod
    def is_collision(coords1, coords2):  # Coords1 is coordinates of individual projectile while Coords2 is coordinates of individual enemies.
        return not (coords1[2] < coords2[0] or coords1[0] > coords2[2] or coords1[3] < coords2[1] or coords1[1] > coords2[3])  # Not (No collision) == There is collision.


# Main menu class
class MainMenu(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Main Menu")
        self.geometry("500x350")

        self.player_name = None
        self.label = tk.Label(self, text="Enter your name:")
        self.label.pack()

        self.entry = tk.Entry(self)  # Textbox to key in player's name
        self.entry.pack(pady=50)

        self.ok_button = tk.Button(self, text="OK", command=self.get_player_name)  # Once button is clicked, get the player's name
        self.ok_button.pack()

    # Method to get player name.
    def get_player_name(self):
        self.player_name = self.entry.get()
        self.destroy()


# Game class, where the game will run.
class Game(tk.Frame):
    def __init__(self, master, player_name):
        super().__init__(master)
        self.width = 600
        self.height = 600
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, bg="black")  # Creates the canvas
        self.canvas.pack()
        self.pack()

        self.projectiles = []
        self.player_lives = 3  # Player only has 3 lives
        self.enemy_counter = 0
        self.timer = 0
        self.line = None

        self.player = Player(self.canvas, master, 285, 555, player_name, self.player_lives)
        self.monster = Monster(self.canvas, 5, self.width, self.canvas.winfo_height())

        self.setup_game()

    # Creates an instance of the Player and the Monster class.
    def setup_game(self):
        # To bind the arrow keys to the move() method in the Player class.
        self.master.bind("<Left>", self.player.move_left)
        self.master.bind("<Right>", self.player.move_right)
        self.master.bind("<Up>", self.player.move_up)
        self.master.bind("<Down>", self.player.move_down)

        self.bind_canvas_events()
        self.create_projectile()
        self.move_projectile()
        self.generate_new_enemies()

    # This method is important to create the red line because apparently the line does not appear when the canvas is initialized. Courtesy of Chatgpt.
    def bind_canvas_events(self):
        self.create_line()
        self.canvas.bind("<Configure>", self.create_line)  # Binds the line to Configure.

    # Creates the red line.
    def create_line(self, event = None):
        self.line = self.canvas.create_line(0, 500, self.canvas.winfo_width(), 500, fill='red', width=2)

    # Creates the projectile.
    def create_projectile(self):
        # Ensures the projectiles spawn in the middle of the player.
        center_x = (self.player.get_position()[0] + self.player.get_position()[2]) / 2
        center_y = (self.player.get_position()[1] + self.player.get_position()[3]) / 2
        projectile = Projectile(self.canvas, center_x, center_y, self.player)
        self.projectiles.append(projectile)  # Adds the projectiles to the list.
        self.after(300, self.create_projectile)  # Calls this function every 0.5 seconds. Basically spawn every projectile every 0.5s.

    # Move the projectiles.
    def move_projectile(self):
        red_line = self.canvas.coords(self.line)[1]  # Get the y coordinate of the line since line is horizontal.
        for projectile in self.projectiles:
            projectile.move(self.monster.enemies)  # Takes in enemies list to check for collision.
        self.monster.move(red_line, self.player, self.timer)  # Call the move() method in the Monster class and takes in the red_line to check if the enemies crossed the red line.
        self.timer += 0.05
        self.after(50, self.move_projectile)  # Calls this funtion every 0.05 seconds

    #     if self.timer >= 45:  # If player lasts for more 45 seconds, he wins.
    #         self.player_wins()
    #
    # # Display win window
    # def player_wins(self):
    #     game_win_label = tk.Label(self.canvas, text="Congratulations! You survived for 45 seconds!", font=("Helvetica", 16), fg="green")
    #     self.canvas.create_window(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2, window=game_win_label)

    # Generates new enemies.
    def generate_new_enemies(self):
        new_enemies = Monster(self.canvas, 1, self.width, 0)
        self.monster.enemies.extend(new_enemies.enemies)  # Adds the new enemies to the back of the enemies list.
        self.enemy_counter += 1
        self.after(1000, self.generate_new_enemies)  # Schedule the next call after 5 seconds


# Needed to run the game.
def main():
    root = tk.Tk()
    root.title('Space Invaders - budget edition')
    main_menu = MainMenu(root)
    root.wait_window(main_menu)

    # Now that the MainMenu window has been closed, create the Game instance.
    game = Game(root, main_menu.player_name)  # Pass the player name as an argument to be used in the Game window.
    game.mainloop()