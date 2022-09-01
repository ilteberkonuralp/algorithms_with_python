class ArrayStack:
    def __init__(self):
        self._data = list() # nonpublic list instance
    def __len__(self): 
        return len(self._data)
    def __getitem__(self):  
        return self._data
    def is_empty(self):
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)

    def extention(self,k):
        self._data.extend(k)
    def top(self):
        if self.is_empty():
            pass
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            pass
        return self._data.pop()





def pathFinder(grid, startX, startY, endX, endY):
    
    path=ArrayStack()
    wrongvisited=ArrayStack()
    tempnode=ArrayStack()
    tempnode.push(startX)
    tempnode.push(startY)
    path.push(list(tempnode._data))
    
    rownum=len(grid)
    colnum=len(grid[0])
    
    tempnode.pop();tempnode.pop()

    while path: 
        tempnode=[path.top()]
        
        i=tempnode[0][0]
        
        j=tempnode[0][1]
        
        
        if(i==endX and j==endY):
            print(*path._data,sep="\n")
            break
        # Down Condition        
        if (i+1<rownum and grid[i+1][j] and ([i+1,j] not in wrongvisited._data) and ([i+1,j] not in path._data)):
            
            tempnode2=ArrayStack()
            tempnode2.push(i+1)
            tempnode2.push(j)
            path.push(list(tempnode2._data))
            
            
        # Right Condition
        elif(j+1<colnum and grid[i][j+1] and ([i,j+1] not in wrongvisited._data) and ([i,j+1] not in path._data)):
            
            tempnode2=ArrayStack()
            tempnode2.push(i)
            tempnode2.push(j+1)
            path.push(list(tempnode2._data))
            
        # Up Condition
        elif(i-1>=0 and grid[i-1][j] and ([i-1,j] not in wrongvisited._data) and ([i-1,j] not in path._data)):
            
            tempnode2=ArrayStack()
            tempnode2.push(i-1)
            tempnode2.push(j)
            path.push(list(tempnode2._data))
            
            
        # Left Condition
        elif(j-1>=0 and grid[i][j-1] and ([i,j-1] not in wrongvisited._data) and ([i,j-1] not in path._data)):
            
            tempnode2=ArrayStack()
            tempnode2.push(i)
            tempnode2.push(j-1)
            path.push(list(tempnode2._data))
            
        else:
            wrongvisited.push(list(tempnode[0]))
            path.pop()
            if (path.is_empty()):
                print("Path not found")
                break
    
    return None



if __name__=="__main__":
    pathFinder([[1,1,1,0,1],[1,1,0,0,1],[1,0,1,1,1],[1,0,0,0,0],[1,1,1,1,0]], 2, 2, 0, 0)
    pathFinder([[1,1,1,1],[1,1,0,0],[1,0,1,0]],2,0,2, 2)
    pathFinder([[0,1,1],[1,0,0],[1,1,1]],2,0,0, 2)
    pathFinder([[1,1,1,0,1],[1,0,0,0,0],[1,1,1,1,0],[0,0,0,1,1],[1,1,0,1,1],[1,1,1,1,1]],0,4,4,0)
    pathFinder([[1,1,1,0],[0,0,1,1],[1,0,0,1],[1,1,1,1]],2,1,0,1)


