import os


def clear_screen():

    os.system("cls" if os.name == "nt" else "clear")  # nt => windows


class Player:
    def __init__(self):
        self.name = None
        self.symbol = None

    def choose_name(self):

        while True:
            player_name = input(" Enter your name (letters only!)").strip()

            if not player_name.isalpha():

                print("name must be letters only!")

            elif len(player_name) < 3 or len(player_name) > 8:
                print("name cannot be less than 3 characters or more than 8 characters")

            elif len(player_name) == 0:
                print("name cannot be empty ")

            else:
                self.name = player_name
                return f"your name now is : {self.name}"

    def choose_symbol(self):

        while True:

            player_symbol = input(f"Hi {self.name} choose  your symbol :")

            if player_symbol.isalpha() and len(player_symbol) == 1:
                self.symbol = player_symbol.upper()
                return f"your symbol is {self.symbol}"
            else:
                print("invalid symbol")


class Menu:

    def display_main_menu(self):

        main_menu_text = """ 
                WELCOME TO TIC TAC TOE GAME..INJOY!

                1.Start Game
                2.Quit Game
                """

        choice = input(main_menu_text)
        return choice

# menu=Menu()
# menu.display_main_menu()

    def display_end_menu(self):
        end_menu_text = """
            Game Over!

            1.Restart Game
            2.Quit Game
            Enter Your Choice (1 or 2) : """

        choice = input(end_menu_text)
        return choice


class Board:

    def __init__(self,):

        self.board_list = [str(i) for i in range(1, 10)]  # list comprehension

    def display_board(self):

        for i in range(0, 9, 3):
            print("|".join(self.board_list[i:i+3]))
            if i < 6:
                print("-"*5)

    # move=input("choose a position to play in : ")

    def is_valid_move(self, choice):

        if self.board_list[choice-1].isdigit():

            return True

# SOLID PRINCIPLES : SINGLE RESPONSIPILITY PRINCIPLE
    def update_board(self, choice, symbol):

        if self.is_valid_move(choice):
            self.board_list[choice-1] = symbol
            return True
        else:
            return False

    def reset_board(self):

        self.board_list = [str(i) for i in range(1, 10)]  # [1,2,3,4,5,6,7,8,9]


class Game_logic:
    def __init__(self):

        self.player = [Player(), Player()]
        self.menu = Menu()
        self.board = Board()
        self.current_player_index = 0

    def start_game(self):

        choice = self.menu.display_main_menu()

        if choice == "1":
            self.setup_players()
            # self.board.display_board()
            self.play_game()

        else:
            self.quit_game()

    def setup_players(self):

        for number, player in enumerate(self.player, start=1):
            print(f" player {number} enter your details : ")
            player.choose_name()
            player.choose_symbol()

            clear_screen()

    def play_game(self):

        while True:
            self.play_turn()

            if self.check_win() or self.check_draw(): 
                choice=self.menu.display_end_menu()
                if choice == "1":
                    self.board.reset_board()
                    self.current_player_index = 0

                else:
                    self.quit_game()
                    break

    def play_turn(self):

        player = self.player[self.current_player_index]

        self.board.display_board()
        print(f"{player.name} 's turn '{player.symbol}' ")

        while True:
            try:
                cell_choice = int(input(" choose a cell (1-9) : "))
                if 1 <= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break

                else:
                
                    print("invalid move, try again")

            except ValueError:
                print("please enter a number between 1-9 . ")

        self.switch_player()

    def switch_player(self):

        self.current_player_index = 1-self.current_player_index

    def check_win(self):
        win_combonatios = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [
                1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combonatios:
            if self.board.board_list[combo[0]] == self.board.board_list[combo[1]] == self.board.board_list[combo[2]]:

                clear_screen()
                print(f"player {self.player[1-self.current_player_index].name} win")
                return True
            
        return False

    def check_draw(self):

            if all(not cell.isdigit() for cell in self.board.board_list):
                clear_screen()
                print ("Draw")
                return True
            return False

    def quit_game(self):

        print("Thank you for playing")

    def restart_game(self):


        self.board.reset_board()
        self.current_player_index = 0
        self.play_game()


game = Game_logic()
game.start_game()



# example=["a","b","c","d","e","f"]

# for i in range(0,6,3):
#     print("|".join(example[i:i+3]))
#     if i<9:
#         print("-"*5)


# # [1,2,3,4,5,6,7,8,9]
# board_list = [str(i) for i in range(1, 10)]  # list comprehension
# for i in range(0, 9, 3):
#     print("|".join(board_list[i:i+3]))
#     if i < 6:
#         print("-"*5)


# def is_valid_move(self,choice):

#     if board_list[choice-1]==int():
#         return choice

# def update_board(self, choice, symbol):

#     move=input("choose a position to play in : ")

#     choice-1==symbol
#     self.board_list[choice-1].replace(str(choice-1),symbol)
# if  is_valid_move == True:
#     print(move)
# else:
#     print("position has taken")
