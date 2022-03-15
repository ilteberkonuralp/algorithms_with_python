"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""


def is_prime(x):
    """Takes x and check whether its a prime number or not.
     Then returns True or False depend on the case."""
    x_sqrt=round(x**(1/2))+1

    for k in range(2,x_sqrt):
        
        if(x%k==0):
            return False
    return True

prime_nums=[]
k=2
while(k<2000000):
    if(is_prime(k)):
        prime_nums.append(k)
    k+=1
print(sum(prime_nums))