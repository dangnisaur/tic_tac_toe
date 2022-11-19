class tac():
    toe = [["*", "*","*"],
            ["*", "*","*"],
            ["*", "*","*"]]
    
    def tic(self):
        for i in range(1, 10):
            a, b=map(int, input("입력하세요 : ").split(" "))
            
            if i%2==0:
                self.toe[a][b] = "X"
            else:
                self.toe[a][b] = "O"
            self.settable()
            self.checkside()
            self.checkslice()
            self.checkup()
    
    def settable(self):
        
        os.system('cls')    
        for i in range (0,3):
            for j in range(0,3):
                print(self.toe[i][j], end=" ")
                print("| " ,end=" ")
            print("\n------------")
    
    def checkside(self):
        for i in range(0,3):
            if self.toe[i][0] == self.toe[i][1] and self.toe[i][1] == self.toe[i][2]:
                if self.toe[i][0] == "X":
                   sys.exit("X가 승리했습니다!")
                elif self.toe[i][0] == "O":
                   sys.exit("O가 승리했습니다!")
                else:
                    return

    def checkup(self):
        
        for i in range(0,3):
            if self.toe[0][i] == 74:
               return
            if self.toe[0][i] == self.toe[1][i] and self.toe[1][i] == self.toe[2][i]:
                if self.toe[0][i] == "X":
                   sys.exit("X가 승리했습니다!")
                elif self.toe[0][i] == "O":
                   sys.exit("O가 승리했습니다!")
                else:
                    return

    def checkslice(self):
        if self.toe[1][1] == 74:
            return
        if self.toe[1][1] == self.toe[0][0] and self.toe[0][0] == self.toe[2][2]:
            if self.toe[1][1] == "X":
                sys.exit("X가 승리했습니다!")
            elif self.toe[1][1] == "O":
                sys.exit("O가 승리했습니다!")
            else:
                return
        if self.toe[1][1] == self.toe[0][2] and self.toe[0][2] == self.toe[2][0]:
            if self.toe[0][2] == "X":
                sys.exit("X가 승리했습니다!")
            elif self.toe[1][1] == "O":
                sys.exit("O가 승리했습니다!")
            else:
                return

import sys
import os
Tac = tac()
Tac.settable()
Tac.tic()
sys.exit("무승부")
