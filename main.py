from random import randint
from random import  seed
import numpy as np
from gui import *
array = np.zeros((4,4))
total = 0
seed(20)
def random_generator():
    row = randint(0,3)
    col = randint(0,3)
    val = 2
    if randint(0,1)==1:
        val=4
    return row,col,val

def initialization():
    row1,col1,val1=random_generator()
    row2,col2,val2=random_generator()
    array[row1][col1]=val1
    array[row2][col2]=val2
    setup(array)

def key(event):
    if event.char == event.keysym:
        msg = '%r' % event.char
    elif len(event.char) == 1:
        msg = '%r (%r)' % (event.keysym, event.char)
    else:
        msg = '%r' % event.keysym
    calculate(msg)
    refresh(array, total)

def push(msg):
    if "Up" in msg:
        for i in range(4):
            temp=[]
            for j in range(4):
                if array[j][i]!=0:
                    temp.append(array[j][i])
                    array[j][i]=0
            for j in range(len(temp)):
                array[j][i]=temp[j]
    elif  "Down" in msg:
        for i in range(4):
            temp=[]
            for j in (3,2,1,0):
                if array[j][i]!=0:
                    temp.append(array[j][i])
                    array[j][i]=0
            for j in range(len(temp)):
                array[3-j][i]=temp[j]
    elif "Left" in msg:
        for i in range(4):
            temp=[]
            for j in range(4):
                if array[i][j]!=0:
                    temp.append(array[i][j])
                    array[i][j]=0
            for j in range(len(temp)):
                array[i][j]=temp[j]
    elif "Right" in msg:
        for i in range(4):
            temp=[]
            for j in (3,2,1,0):
                if array[i][j]!=0:
                    temp.append(array[i][j])
                    array[i][j]=0
            for j in range(len(temp)):
                array[i][3-j]=temp[j]
    return

def calculate(msg):
    if "Up" in msg:
        for i in range(4):
            for j in range(3):
                if array[j+1][i]==0:
                    last=array[j][i]
                    old_j=j
                    j=j+1
                    while array[j][i]==0 and j<3:
                        j+=1
                    if array[j][i] == last:
                        array[old_j][i] = 2 * array[old_j][i]
                        global total
                        total= total + array[old_j][i]
                        array[j][i]=0
                else:
                    if array[j][i]==array[j+1][i]:
                        array[j][i]=2*array[j][i]
                        total= total + array[j][i]
                        array[j+1][i]=0
                        j+=1

    elif "Down" in  msg:
        for i in range(4):
            for j in (3,2,1):
                if array[j-1][i]==0:
                    last=array[j][i]
                    old_j=j
                    j=j-1
                    while array[j][i]==0 and j>0:
                        j-=1
                    if array[j][i] == last:
                        array[old_j][i] = 2 * array[old_j][i]
                        total= total + array[old_j][i]
                        array[j][i]=0
                else:
                    if array[j][i]==array[j-1][i]:
                        array[j][i]=2*array[j][i]
                        total= total + array[j][i]
                        array[j-1][i]=0
                        j-=1
    elif "Left" in msg:
        for i in range(4):
            for j in range(3):
                if array[i][j+1]==0:
                    last=array[i][j]
                    old_j=j
                    j=j+1
                    while array[i][j]==0 and j<3:
                        j+=1
                    if array[i][j] == last:
                        array[i][old_j] = 2 * array[i][old_j]
                        total= total + array[i][old_j]
                        array[i][j]=0
                else:
                    if array[i][j]==array[i][j+1]:
                        array[i][j]=2*array[i][j]
                        total= total + array[i][j]
                        array[i][j+1]=0
                        j+=1

    elif "Right" in  msg:
        for i in range(4):
            for j in (3,2,1):
                if array[i][j-1]==0:
                    last=array[i][j]
                    old_j=j
                    j=j-1
                    while array[i][j]==0 and j>0:
                        j-=1
                    if array[i][j] == last:
                        array[i][old_j] = 2 * array[i][old_j]
                        total= total + array[i][old_j]
                        array[i][j]=0
                else:
                    if array[i][j]==array[i][j-1]:
                        array[i][j]=2*array[i][j]
                        total= total + array[i][j]
                        array[i][j-1]=0
                        j-=1
    else:
        return
    push(msg)
    # randomly filling one block
    row,col,val=random_generator()
    while array[row][col]!=0:
        row, col, val = random_generator()
    array[row][col]=val

def main():
    initialization()
    window.bind_all('<Key>', key)
    window.mainloop()

if __name__ == "__main__":
    main()