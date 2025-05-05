# The code is designed to "reverse" SHA-256 hash values back to their
# original 4-digit numbers.
# This is essentially a simple password cracking technique
# for a very specific case,
# when you know the passwords are 4-digit numbers.

import hashlib
import csv

# In this function, you have to give two CSV files as input
# to read the information from one and save the output in another


def hash_password_hack(input_file_name, output_file_name):

    hashObject = hashlib.sha256()

    hashAnswers = dict()
    for i in range(1000, 10000):
        hashObject.update(str(i).encode())
        hashAnswers[hashObject.hexdigest()] = str(i)

    with open(input_file_name, 'r') as input_file:
        for row in csv.reader(input_file):
            second_input_file = open(output_file_name, 'a')
            second_input_file.write("%s,%s\n" % (row[0], hashAnswers[row[1]]))
