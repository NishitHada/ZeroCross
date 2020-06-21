class Board:
    def __init__(self):
        self.arr = [[-1 for i in range(3)] for j in range(3)]

    def __init__(self, state):
        self.arr = [[-1 for i in range(3)] for j in range(3)]
        for i in range(0, 3):
            for j in range(0, 3):
                self.arr[i][j] = state[i][j]

    def print_board(self):
        print(self.arr)

    def update(self, row, col, sign):
        if sign not in range(1):
            return 1
        if row in range(3) and col in range(3):
            self.arr[row][col] = sign
            return 0
        else:
            return 1

    def check_state(self):
        #row check
        for i in range(3):
            if self.arr[i][0] == self.arr[i][1] and self.arr[i][1] == self.arr[i][2]:
                return self.arr[i][0]

        #col check
        for j in range(3):
            if self.arr[0][j] == self.arr[1][j] and self.arr[1][j] == self.arr[2][j]:
                return self.arr[0][j]

        #diag check
        if self.arr[0][0] == self.arr[1][1] and self.arr[1][1] == self.arr[2][2]:
            return self.arr[0][0]

        if self.arr[0][2] == self.arr[1][1] and self.arr[1][1] == self.arr[2][0]:
            return self.arr[2][0]

        game_flag = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.arr[i][j] == -1:
                    game_flag = 1

        #There's an empty cell
        if game_flag == 1:
            return 2
        #Tie case
        return 3
