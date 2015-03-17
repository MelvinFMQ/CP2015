def is_palindrome(string):
    if string == '':
        return True
    return string[-1].lower() == string[0].lower() and is_palindrome(string[1:len(string)-1])

#lower case and upper case test 
print(is_palindrome('Wow'))

#normal case
print(is_palindrome('wew'))

#fail case
print(is_palindrome('eeew'))
