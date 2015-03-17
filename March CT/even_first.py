def even_first(num):#num is an interger, iterative
    string = str(num)
    even = []
    odd = []
    for letter in string:
        num_letter = int(letter)
        if num_letter % 2 == 0: #even num
            print('even')
            even.append(letter)
        else:
            odd.append(letter)
    even = sorted(even)
    odd = sorted(odd)   
    return_string = ''
    print(even)
    print(odd)
    for letter in even:
        return_string += letter
    for letter in odd:
        return_string += letter
    return return_string


print(even_first(56789))
        
#recursive
def even_first(num):
    if num == 0:
        return ''
    highest_digit = num // 10 ** (len(str(num))-1)
    rest_of_digit = num % 10 ** (len(str(num))-1)
    print('high', highest_digit)
    print('rest', rest_of_digit)
    if highest_digit % 2 == 0: #even
        return int(str(highest_digit) + str(even_first(rest_of_digit)))
    else: #odd
        return int(str(even_first(rest_of_digit)) + str(highest_digit))

print(even_first(56789))

        
            
            
    
       
            
            
    
