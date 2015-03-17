def generator(num):
    for i in range(num):
        yield i

for i in generator(10):
    print(i)

def generator2(num):
    i = 0
    while i < num:
        i += 1
        yield i
        yield 'yo'

for i in generator2(10):
    print(i)
         
