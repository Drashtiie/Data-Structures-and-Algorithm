

board = [["O","O","O"],["O","O","O"],["O","O","O"]]

n = len(board[0])
m = len(board)
v = [[0 for x in range(n)] for y in range(m)]
q=[]
for i in range(m):
    if board[i][0] == 'O' and v[i][0] == 0:
        v[i][0] = 1
        q.append([i,0])
       
    if board[i][n-1] == 'O' and v[i][n-1] == 0:
        v[i][n-1] = 1
        q.append([i,n-1])

for j in range(n):
    if board[0][j] == 'O' and v[0][j] == 0:
        v[0][j] = 1
        q.append([0,j])
    if board[m-1][j] == 'O' and v[m-1][j] == 0:
        v[m-1][j] = 1
        q.append([m-1,j])

while q:
        x,y = q.pop(0)
        # print(x,y)
        v[x][y] = 1
        l1 = [-1,0,1,0]
        l2= [0,-1,0,1]
        for i in range(4):
            x1 = x + l1[i]
            y1 = y + l2[i]
            # print(x1,y1)
            if x1 > 0 and y1>0 and x1<m-1 and y1<n-1 and board[x1][y1] == "O" and v[x1][y1] == 0:
                
                q.append([x1,y1])
                v[x1][y1] = 1

for i in range(m):
        for j in range(n):
            if v[i][j] == 0:
                board[i][j] = "X"

