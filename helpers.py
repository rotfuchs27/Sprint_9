import random
import string

#Генерация данных для случайного пользователя
class DataGeneration:

    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    def generate_random_email():
        email = f"user{random.randint(1000, 9999)}@example.com"
        return email