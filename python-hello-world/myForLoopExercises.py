
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if (number%i == 0):
            return False

    return True


def sum_up_to(number):
    result = 0
    for i in range(1, number+1):
        result += i
    return result


def sum_of_divisors(number):
    sumofdivs = 0
    for i in range(2, number):
        if number%i == 0:
            sumofdivs += i
    return sumofdivs


def print_number_triangle(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(f"{j}", end=' ')
        print()


print(is_prime(1))
print(is_prime(3))
print(is_prime(16))
print(is_prime(17))

print(sum_up_to(13))
print(sum_of_divisors(14))
print_number_triangle(4)