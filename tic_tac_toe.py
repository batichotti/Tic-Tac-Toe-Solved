class TicTacToe:
    def __init__(self):
        self.tic_tac_toe = [
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]
        self.empty_cells = list(range(9))

    def print_game(self):
        for i in range(2):
            print(f"{self.tic_tac_toe[i][0]} | {self.tic_tac_toe[i][1]} | {self.tic_tac_toe[i][2]}")
            print("──────────")
        print(f"{self.tic_tac_toe[2][0]} | {self.tic_tac_toe[2][1]} | {self.tic_tac_toe[2][2]}\n")
        
    def input_move(self, string: str) -> int:
        try:
            move = input(string)
            while True:
                if move == "":
                    move = input(string)
                    continue
                if move.isnumeric() and int(move) - 1 in self.empty_cells:
                    break
                print("Invalid Move, try again.")
                move = input(string)
        except KeyboardInterrupt:
            print("\nClosing by Keyboard Interruption")
            exit(0)
        except Exception as e:
            print(e)
        return int(move)-1
    
    def check_lines(self, move: int) -> bool:
        win = (True) if (self.tic_tac_toe[move//3][0] == self.tic_tac_toe[move//3][1] == self.tic_tac_toe[move//3][2] != '_') else (False)
        return win

    def check_columns(self, move: int) -> bool:
        win = (True) if (self.tic_tac_toe[0][move%3] == self.tic_tac_toe[1][move%3] == self.tic_tac_toe[2][move%3] != '_') else (False)
        return win

    def check_diagonals(self, move: int) -> bool:
        win = (True) if (self.tic_tac_toe[0][0] == self.tic_tac_toe[1][1] == self.tic_tac_toe[2][2] != '_') else (False)
        return (win or (self.tic_tac_toe[0][2] == self.tic_tac_toe[1][1] == self.tic_tac_toe[2][0] != '_'))
        
    def play(self):
        turn = 0
        self.print_game()
        while turn <= 9 and len(self.empty_cells):
            if turn % 2:
                move = self.input_move("[1, 9]: O -> ")
            else:
                move = self.input_move("[1, 9]: X -> ")

            self.tic_tac_toe[move//3][move%3] = ("O") if (turn % 2) else ("X")
            self.empty_cells.remove(move)
            self.print_game()
            
            win = self.check_lines(move) or self.check_columns(move)
            if not (move%2): win = win or self.check_diagonals(move)
            
            if win:
                print(f"{("O") if (turn%2) else ("X")} WIN!")
                break
            
            turn += 1
        if not win: print("DRAW!")


game = TicTacToe()

if __name__ == '__main__':
    print("Tic Tac Toe")
    game.play()
