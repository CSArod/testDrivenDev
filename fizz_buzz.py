
def fizz_buzz():

    result = []

    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            result.append("Fizzbuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(num)

    
    return result


    
    
fizz_buzz()

