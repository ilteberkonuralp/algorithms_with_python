"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
def is_prime(x):
    x_Sqrt=round(x**(1/2))
    for k in range(2,x_Sqrt+1):
        if(x%k==0):
            return False

    return True
prime_list=[]
val=2
while len(prime_list)<10001:
    if (is_prime(val)):
        prime_list.append(val)
        val+=1
    else:
        val+=1
print(prime_list[-1])