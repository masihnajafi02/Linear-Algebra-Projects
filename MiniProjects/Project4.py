import numpy as np

def ToReducedRowEchelonForm( M):
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i],M[r] = M[r],M[i]
        lv = M[r][lead]
        M[r] = [ mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [ iv - lv*rv for rv,iv in zip(M[r],M[i])]
        lead += 1
 
theInput=input().split()
m=int(theInput[0])
n=int(theInput[1])
a=[]
for i in range(n):
    a.append(np.array(input().split(), dtype=float)) 
ToReducedRowEchelonForm( a )
 
rank = len(a)
for row in a:
    if not(np.any(row)):
        rank -= 1

print(rank)