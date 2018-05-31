import random
from board import Board
from btree import Tree

class Game():
    def __init__(self):
        self.first_name = str(input("Enter name of first player: "))
        self.second_name = str(input("Enter name of second player: "))
        self.first_step = random.randint(1, 2)
        self.position = None
        self.count = 1
        self.board = Board().board

    def check(self):
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[0] != None and self.board[1] != None and self.board[2]!= None:
                return True
        elif self.board[0] == self.board[4] == self[8]:
            if self.board[0] != None and self.board[4] != None and self.board[8] != None:
                return True
        elif self.board[2] == self.board[4] == self.board[6]:
            if self.board[2] != None and self.board[4] != None and self.board[6] != None:
                return True
        elif self.board[0] == self.board[3] == self.board[6]:
            if self.board[0] != None and self.board[3] != None and self.board[6] != None:
                return True
        elif self.board[3]==self.board[4]==self.board[5]:
            if self.board[3] != None and self.board[4] != None and self.board[5] != None:
                return True
        elif self.board[6]==self.board[7]==self.board[8]:
            if self.board[6] != None and self.board[7] != None and self.board[8] != None:
                return True
        elif self.board[2]==self.board[5]==self.board[8]:
            if self.board[2] != None and self.board[5] != None and self.board[8] != None:
                return True
        else:
            return False

    def start_game(self):
        a = False
        while a == False:
            if Tree().height() == True:
                print("It's your step, {}. You are 'X'".format(self.first_name))
                try:
                    self.position = int(input('Enter cells position: '))
                except ValueError:
                    print("Please try again")
                if self.position>0 and self.position <=9:
                    if self.board[self.position-1] == None:
                        self.board[self.position-1] = 'X'
                        self.print_board()
                        self.count += 1
                        Tree().insert('O')
                    else:
                        raise ValueError('Try again')
                else:
                    raise ValueError('Try again')

            else:
                print("It's your step, {}. You are 'O'".format(self.second_name))
                try:
                    self.position = int(input('Enter cells position: '))
                except ValueError:
                    print("Please try again")
                if self.position>0 and self.position <=9:
                    if self.board[self.position - 1] == None:
                        self.board[self.position-1] = 'O'
                        self.print_board()
                        self.count += 1
                        Tree().insert('O')
                    else:
                        raise ValueError('Try again')
                else:
                    raise ValueError('Try again')
            if self.check() == True:
                break
        print("You win")


    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])



if __name__=='__main__':
    Game().start_game()




