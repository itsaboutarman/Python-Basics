from collections import deque

# we capitalize the constant names
PI = 3.14


numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4]
first, second, *other = numbers
print(first)
print(other)


# map
items = [('item1', 1), ('item2', 2), ('item3', 3)]
prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]  # best practice
# filter
filtered_items = list(filter(lambda item: item[1] >= 2, items))
filtered_items = [item for item in items if item[1] >= 2]  # best practice
# zip
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip("abc", list1, list2)))


# to use stack we use list but for queue we use deque
queue = deque([])  # You must import deque from collections
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()


# set
first_set = {1, 2, 3, 4, 5}
second_set = {1, 10}
print(first_set - second_set)  # difference
print(first_set | second_set)  # union
print(first_set & second_set)  # intersection
print(first_set ^ second_set)  # symmetric difference


# dictionary
first_dictionary = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}

second_dictionary = {x: x * 2 for x in range(5)}
third_dictionary = dict(one=1, two=2, three=3)


# unpacking
values = [*range(5), *"Hello"]  # to unpack iterables we use *

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}  # to unpack dictionaries we use **


# packing the arguments
def multiply(*list):  # to pack the arguments we use *
    result = 1
    for item in list:
        result *= item
    return result


print(multiply(1, 2, 3, 4))


def save_user(**user):  # to pack the keyword arguments(dictionaries) we use **
    print(user)


save_user(id=1, name="John", age=22)

#########################################################################################
# Exercise: find the most repeated character in this string
sentence = "This is a common interview question"

# Answer:
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pritn(max(char_frequency, key=char_frequency.get))
