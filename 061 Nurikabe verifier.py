def verify(puzzle):
    m = len(puzzle)
    n = len(puzzle[0])
    
    def verifydots(puzzle):
        for i in range(m-1):
            for j in range(n-1):
                if puzzle[i][j] == '.' and puzzle[i][j+1] == '.' and puzzle[i+1][j]== '.' and puzzle[i+1][j+1] == '.':
                    return False
                return True
    
    def checkfordifferent(puzzle):
        allowedSymbols = ['#', '.', 2]
        
        for i in range(m):
            for j in range(n):
                if puzzle[i][j] not in allowedSymbols:
                    return True
        
                return False
    
    if verifydots(puzzle) and checkfordifferent(puzzle):
        return True
    else:
        return False
            
