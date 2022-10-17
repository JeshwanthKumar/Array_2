#Time_Complexity: O(m*n)
#Space_Complexity: O(1)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dir_array = [[0,1], [1,0],[-1,0],[-1,1],[0,-1],[-1,-1],[1,-1],[1,1]]    #Initialize dir_array to store all the directions of its neighboring elements
        
        m = len(board)  #Lenght of rows
        n = len(board[0])   #Length of columns
       
        
        for i in range(m):  #Continue till the length of rowws
            for j in range(n):  #Continue till the length of columns
                count = 0   #Initalize count ot 0

                for r, c in dir_array:  #For r and c in dir_array
                    nr = r+i    #nr is the neighboring row 
                    nc = c+j    #nc is the neighboring column
                    
                    
                    if nr >= 0 and nr < m and nc >= 0 and nc < n:   #If nr is greater than or equal to 0 and less than m and nc is greater than or equal to 0 and less than n
                        if board[nr][nc] == -1 or board[nr][nc] == 1:   #If board[nr][nc] is equal to -1 or board[nr][nc] is equal to 1 increment the count by 1
                            count+=1
                            
                if board[i][j] == 1:    #If the board[i][j] is equal to 1 and if conut is less than 2 or greater than 3 change the value in the board to -1
                    if count < 2 or count > 3:
                        board[i][j] = -1
                        
                else:   
                    if count == 3:  #Else if the count is equal to 3 change the value in the board to 2
                        board[i][j] = 2
                        
        for i in range(m):  #For the length of rows continue the loop
            for j in range(n):  #For the length of columns continue the loop
                if board[i][j] == -1:   #If board[i][j] is equal to -1 change tha value to 0
                    board[i][j] = 0
                elif board[i][j] == 2:  #Else if board[i][j] is equal to 2 change the value to 0
                    board[i][j] = 1
                    
            