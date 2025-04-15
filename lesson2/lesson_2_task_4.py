num = int(input('Enter a number: '))

def fizz_buzz(num: int) -> str:
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return 'Buzz'

print(fizz_buzz(num))
