# Prime Number API
API for requesting computed primes and queuing prime number computations.

Project for own entertainment.

POST HTTP

http://your-ip:20044/queue

Body of request - JSON:

{
    "num_calc": 5
}

Return:

Success

GET HTTP 

http://your-ip:20044/get_primes

1
2
3
5
7
