#Q2
def reversal(string):
    if len(string) == 1:
        return string
    return string[-1] + reversal(string[:(len(string)-1)])

#normal test case
print(reversal('yooooo'))

#symatrical case
print(reversal('1234321'))
