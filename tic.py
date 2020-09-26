import random
lis=[1,2,3,4,5,6,7,8,9]
players=['O','X']
def grid(lis):
    for i in range(1,len(lis)+1):
        if i%8==0:
            pass
        elif i%4==0 or i%7==0:
            print('\n')
        print(lis[i-1],'_|',end="")

grid(lis)
print("\n")
#game main
def gameTurnfirst():
    turn=random.randint(0,len(players)-1)
    while True:
        if players[turn]=='O' or players[turn]=='X':
           print(f"{players[turn]} chance to take a move\n")
           pos=input('enter the place where u want to place value')
           pos=int(pos)
           if lis[pos - 1] == 'X' or lis[pos - 1] == "O":
               print('enter another location to take a move')
               grid(lis)
               continue
           lis[pos-1]=players[turn]
           grid(lis)
           print("\n")
           if turn==0:
              turn=1
           elif turn==1:
              turn=0
           if lis[0]==lis[1]==lis[2]=="X" or lis[1]==lis[4]==lis[7]=="X" or lis[0]==lis[4]==lis[8]=="X" or lis[6]==lis[7]==lis[8]=="X" or lis[2]==lis[5]==lis[8]=="X" or lis[2]==lis[4]==lis[6]=="X":
               print("X won the game ")
               break
           elif (lis[0]=="X" or lis[0]=="O") and (lis[1]=="X" or lis[1]=="O")and (lis[2]=="X" or lis[2]=="O") and (lis[3]=="X"or lis[3]=="O") and (lis[4]=="X" or lis[4]=="O") and (lis[5]=="X" or lis[5]=="O")and (lis[6]=="O" or lis[6]=="X")and(lis[7]=="X"or lis[7]=="O")and(lis[8]=="X" or lis[8]=="O"):
               print('match is drawn play again')
               break
           elif lis[0]==lis[1]==lis[2]=="O" or lis[1]==lis[4]==lis[7]=="O" or lis[0]==lis[4]==lis[8]=="O" or lis[6]==lis[7]==lis[8]=="O" or lis[2]==lis[5]==lis[8]=="O" or lis[2]==lis[4]==lis[6]=="O":
               print('O won the game')
               break

gameTurnfirst()