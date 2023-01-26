import random


def generate_random(counter=50, number_range=100) -> list:
    """
    This function generates random numbers
    :param number_range: range of the random number
    :param counter: length of random numbers
    :return: list o f random numbers
    """
    r_list = []
    for i in range(counter):
        rand_number = random.randint(0, number_range)
        r_list.append(rand_number)
    return r_list


def check_even_odd(random_list: list):
    """
    This function returns odd and even number
    :param random_list: list of random integers
    :return: list of even and odd numbers
    """
    even_list = []
    odd_list = []
    for number in random_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list


def check_prime_number(num: int) -> bool:
    """
    check if the number is prime or not
    :param num: number to be checked
    :return: boolean value for prime number
    """
    if num == 1:
        return True
    for item in range(2, num):
        if num % item == 0:
            return False
    return True


if __name__ == '__main__':
    random_numbers = generate_random(counter=300, number_range=2000)
    even, odd = check_even_odd(random_numbers)
    print(even)
    print(odd)
    print(f'type of the following variables is {type(random_numbers)} -- {type(even)} -- {type(odd)}')
    print(f'the length of the variables are {len(random_numbers)} -- {len(even)} -- {len(odd)}')

    number = 4
    if check_prime_number(number):
        print(f'{number}  is prime')
    else:
        print(f'{number} is not prime')
