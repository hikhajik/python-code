# Program to find prime numbers up to a given number1

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # check divisibility up to sqrt(num)
        if num % i == 0:
            return False
    return True

def find_primes(limit):
    """Return a list of prime numbers up to the given limit."""
    primes = []
    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)
    return primes

# Example usage
limit = int(input("Enter the upper limit: "))
prime_numbers = find_primes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")





