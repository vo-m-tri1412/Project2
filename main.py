def sortArray(numbers):
    return sorted(numbers)


def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def countPrimes(numbers):
    return sum(1 for number in numbers if isPrime(number))


def main():
    input_str = input("Enter a list of numbers separated by space: ")
    numbers = [int(num) for num in input_str.split()]
    print("The list of numbers is:", numbers)
    if numbers:
        num_to_check = numbers[0]
        if isPrime(num_to_check):
            print(f"{num_to_check} is a prime number.")
        else:
            print(f"{num_to_check} is not a prime number.")
    print("The number of prime numbers is:", countPrimes(numbers))
    print("The sorted array is:", sortArray(numbers))


if __name__ == "__main__":
    main()
