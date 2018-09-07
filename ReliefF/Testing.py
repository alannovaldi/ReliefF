from ReliefF import ReliefF
import numpy as np

columnNum = int(input())
rowNum = int(input())

matrix = np.zeros((rowNum,columnNum))

labelContents = []

i = 0

while i < rowNum:
  #todo: set input to matrix
  row = input()
  rowContents = row.split()
  j = 0
  
  for content in rowContents:
  	matrix[i][j] = content
  	j += 1
  labelContents.append(i+1)
  i += 1


#print(matrix)
#print(matrix[252][7])

testingData = ReliefF()
testingData.fit(matrix, labelContents)
print(testingData.transform(matrix))