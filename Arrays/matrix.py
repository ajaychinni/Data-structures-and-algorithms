def mat_prob(mat):
    rotten = []
    for i in range (len(mat)):
        for j in range(len(mat[0])):
            if i == 0 or j == 0 or i == len(mat)-1 or j == len(mat[0]) -1:
                continue
            else:
                if mat[i-1][j] < mat[i][j] and mat[i+1][j] < mat[i][j] \
                and mat[i][j-1] < mat[i][j] and mat[i][j+1] < mat[i][j]:
                    rotten.append({mat[i][j]:(i,j)})

    return rotten
print(mat_prob([[1,2,3,5,9],[1,4,36,0,6],[34,7,32,38,9],[2,4,26,0,6]]))
