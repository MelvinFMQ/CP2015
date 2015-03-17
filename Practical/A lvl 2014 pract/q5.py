def smallest_multiple(num):
    primes = []
    for i in range(2, num+1):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    double = []
    for prime in primes:
        product = 1
        pwr = 2
        while product < num:
            product = prime ** pwr
            if product < num:
                double.append(prime)
            pwr += 1
            
    facts = double + primes
    total = 1
    for fact in facts:
        total = total * fact
    print(total)
    
smallest_multiple(20)
