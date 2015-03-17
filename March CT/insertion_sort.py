def insertion_sort(a): # array to be pass in
    new_a = [a[0]]
    for i in range(1, len(a)):
        thing_to_insert = a[i]
        print('Thing to insert', thing_to_insert)
        j = 0
        #keep going right until elements are bigger than the new element 
        while j < len(new_a) and new_a[j] < thing_to_insert:
            print('j', j)
            print(new_a)
            j += 1
        new_a.insert(j, thing_to_insert)
    return new_a

print(insertion_sort([1,5,7,3,4,9]))
    
