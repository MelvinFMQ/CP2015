def has_more_vowels(string):
    vowels = ['a', 'e', 'i' , 'o' , 'u']
    vowels_count = 0
    if string.replace(' ', '').isalpha():
        string = string.lower()
    else:
        print('Invalid input')
        return 
    for vowel in vowels:
        vowels_count += string.count(vowel)
    consonants = len(string) - vowels_count

    return vowels_count > consonants

#more vowels
print(has_more_vowels('Google IO'))

#less vowels
print(has_more_vowels('Apple WWDC'))

#equal
print(has_more_vowels('iv'))

#recursive
def has_more_vowels(string, num_vowel=0, num_consonants=0):
    if string == '':
        return num_vowel > num_consonants
    vowels = ['a', 'A', 'E', 'e', 'I', 'i' , 'O', 'o' , 'U', 'u']
    string = string.replace(' ' , '')
    if string[0] in vowels:
        return has_more_vowels(string[1:], num_vowel + 1, num_consonants)
    else:
        return has_more_vowels(string[1:], num_vowel, num_consonants+1)

#more vowels
print(has_more_vowels('Google IO'))

#less vowels
print(has_more_vowels('Apple WWDC'))

#equal
print(has_more_vowels('iv'))
