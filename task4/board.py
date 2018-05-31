from array import Array

class Board():
    def __init__(self):
        board= Array(9)
        self.board = board
        self.step = None
        self.point = None

    def check(self):
        if self.board[0] == self.board[1] == self.board[2]:
            if self.board[0] != None and self.board[1] != None and self.board[2]!= None:
                return True
        elif self.board[0] == self.board[4] == self.board[8]:
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


if __name__=="__main__":
    a = Board()
    a.check()
