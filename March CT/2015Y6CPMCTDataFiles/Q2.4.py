#Q2.4
def even_first(num, index=0, count = 0):
    string = str(num)
    if int(string[index]) % 2 == 0: #even
        return string[index] + even_first(int(string[1:], index + 1))
    else: #odd
        return even_first(int(string[1:], index + 1)) + string[index]


even_first(12)                                  
        
                            
    
    
