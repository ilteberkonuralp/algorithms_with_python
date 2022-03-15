"""The sum of the squares of the first ten natural numbers is,
                sum((1:10)^2)=385
The square of the sum of the first ten natural numbers is,
                    sum(1:10)^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is .
                3025-385=2640
Find the difference between the sum of the squares of the first one hundred natural
 numbers and the square of the sum."""
def square_of_sum(x=100):
    """The function calculates the square the of sum until that number."""
    res=0
    for k in range(x+1):
        res+=k
    return res**2
def sum_of_square(x=100):
    """The function calculates the sum of the squared values until that number."""
    res=0
    for k in range(x+1):
        res+=k**2
    return res

square_of_sums=sum([i for i in range(1,101)])**2
sum_of_squares=sum([i**2 for i in range(1,101)])
print(square_of_sums-sum_of_squares)
print(square_of_sum()-sum_of_square())