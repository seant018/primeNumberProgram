import math, sys


def main():
    # requires a file named "data.txt", which must have a number only
    f = open("data.txt")
    num = int(f.read())
    f.close()

    while True:
        if isPrime(num):
            with open("data.txt", "w") as f:
                f.write(str(num))
            print(str(num) + ", \n", end="", flush=True)
        num = num + 1


def isPrime(number):
    # Return True if the number is prime, otherwise False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
