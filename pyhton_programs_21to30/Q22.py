#Determine if a number is a prime number.
def is_prime(number):
# Prime numbers are greater than 1
  if number <= 1:
    return False

  # 2 is the only even prime number
  if number == 2:
    return True

  # All other even numbers are not prime
  if number % 2 == 0:
    return False

  # Check for divisibility from 3 up to the square root of the number,
  # incrementing by 2 (to check only odd divisors).
  # We only need to check up to the square root because if a number `n`
  # has a divisor `d > sqrt(n)`, then it must also have a divisor `n/d < sqrt(n)`.
  i = 3
  while i * i <= number:
    if number % i == 0:
      return False
    i += 2

  # If no divisors were found, the number is prime
  return True