import random
from typing import List


def random_numbers(counter=50, number_range=100) -> list:
    """
    making function of random numbers
    1. need 50 random numbers from 100 numbers
    2. create a random list
    3. random_list[] is empty
    4. created a loop for 50 random numbers out of 100
    5. implementing random function
    :param counter:
    :param number_range:
    :return:
    """

    random_list: list[int] = []
    for i in range(counter):
        rand_number = random.randint(0, number_range)
        random_list.append(rand_number)
    return random_list


def check_even_odd_numbers(random_list: list) -> list:
    """
    This function will check even & odd numbsers
    :param random_list:
    :return: list of even & odd numbers
    """
    odd_num = []
    even_num = []
    for number in random_list:
        if number % 2 == 0:
            even_num.append(number)
        else:
            odd_num.append(number)
    return even_num, odd_num


def prime_list(random_list: list) -> list:
    prime_num = []
    for number in random_list:
        is_prime = True
        if number == 1:
            prime_num.append(number)
        for check in range(2, number):
            if number % check == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(number)
    return prime_num


if __name__ == '__main__':
    print(random_numbers())  # Calling function in print()

    list_random_number = random_numbers()
    even_number, odd_number = check_even_odd_numbers(random_list=list_random_number)
    print(even_number)
    print(odd_number)
    print(sorted(prime_list(list_random_number)))
    print(f'Following variables is {type(even_number)} - - {type(odd_number)} - - {type(list_random_number)}')
    print(f'length of the list is {len(even_number)} - - {len(odd_number)} -- {len(list_random_number)}')


