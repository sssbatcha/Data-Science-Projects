rows,cols=2,2
matrixA=[[5,4],[3,5]]
matrixB=[[2,3],[1,2]]
res = [[0,0],[0,0]]
for r in range(rows):
    for c in range(cols):
        res[r][c]=matrixA[r][c]-matrixB[r][c]
for row in res:
    print(" ".join(map(str,row)))