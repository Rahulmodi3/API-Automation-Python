import random
import logging as logger


def generate_random_firstname_and_lastname():
    """ For generate random firstname and lastname """

    first_names = ['John', 'Andy', 'Joe', 'George', 'Shawn', 'Robert', 'Steven']
    last_names = ['Rios', 'Smith', 'Williams', 'Manning', 'Harrell', 'White', 'Miller']

    firstname = ''.join(random.choices(first_names))
    lastname = ''.join(random.choices(last_names))

    random_info = {'firstname': firstname, 'lastname': lastname}
    logger.info(f"Randomly generated firstname and lastname: {random_info}")

    return random_info



