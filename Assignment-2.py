import random
k={}
def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    end = False
    win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    list1=[1,2,3,4,5,6,7,8,9]
    def draw():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])
        print()

    def p1():
        n = choose_number()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p1()
        else:

            board[n] = "X"

    def p2():
        n = random.choice(list1)
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            p2()
        else:
            board[n] = "O"

    def choose_number():
        while True:
            while True:
                a = input()
                try:
                    a = int(a)
                    a -= 1
                    if a in range(0, 9):
                        return a
                    else:
                        print("\nThat's not on the board. Try again")
                        continue
                except ValueError:
                    print("\nThat's not a number. Try again")
                    continue

    def check_board():
        count = 0
        for a in win_combinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("Player Wins!\n")
                print("Congratulations!\n")
                board[9]=0
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("Computer Wins!\n")
                print("Congratulations!\n")
                board[9]=1
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends in a Tie\n")
                return True

    while not end:
        draw()
        end = check_board()
        temp=board

        if end == True:
            break
        print("Player 1 choose where to place a cross")
        p1()
        print()
        draw()
        end = check_board()
        if end == True:
            break
        print("Player 2 choose where to place a nought")
        p2()
        print()
    return board
i=0
while i<10:
    i+=1
    x=tic_tac_toe()
    k[i]=x
u=int(input("ENTER THE ROUND :"))
v=u-1
y=k[u]
print(y[0], y[1], y[2])
print(y[3], y[4], y[5])
print(y[6], y[7], y[8])
if(y[9]==0):
    print("PLAYER WON ROUND {}".format(v))
else:
    print("COMPUTER WON ROUND {}".format(v))