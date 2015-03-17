def swap(string, index=0):
    if string == '':
        return ''
    return string[index+1] + string[index] + swap(string[2:])

#normal
print(swap('hiyo'))
