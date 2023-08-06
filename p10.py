
X = [[12,7],
    [4 ,5]]

Y = [[5,8],
    [6,70],]

result = [[0,0],
         [0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
