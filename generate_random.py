import random


def generate_random(counter=50, number_range=100) -> list:
    """
    This method generates random numbers
    :param number_range: range of the random number
    :param counter: length of random numbers
    :return: list of random numbers
    """
    r_list = []
    for i in range(counter):
        rand_number = random.randint(0, number_range)
        r_list.append(rand_number)
    return r_list


def check_even_odd(random_list: list):
    even_list = []
    odd_list = []
    for number in random_list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)

    return even_list, odd_list


if __name__ == '__main__':
    random_numbers = generate_random(counter=300,number_range=2000)
    even, odd = check_even_odd(random_numbers)
    print(even)
    print(odd)
    print(f'type of the following variables is {type(random_numbers)} -- {type(even)} -- {type(odd)}')
    print(f'the length of the variables are {len(random_numbers)} -- {len(even)} -- {len(odd)}')
