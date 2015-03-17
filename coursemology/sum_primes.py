def sum_primes(num):
    # Write your function code here
    #total = 2
    primes_array = [2]
    for interger in range(3, num, 2):
#        div = 3
        no_to_test_till = int(interger ** 0.5)
        is_prime = True
#        while div < no_to_test_till + 1:
#            if interger % div == 0:
#                is_prime = False
#                break
#            div += 2
        for prime in primes_array:
            if prime > no_to_test_till:
                break
            if interger % prime == 0:
                is_prime = False
                break
        if is_prime:
            #total += interger
            primes_array.append(interger)
            
    return sum(primes_array) 
print(sum_primes(2000000))
