# Q1 . **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
    # - *Input*: [("John", 25), ("Jane", 30)]
    # - *Output*: "John is 25 years old. Jane is 30 years old."

def print_names_and_ages(name_age_list):
    for name, age in name_age_list:
        print(f"{name} is {age} years old.")


name_age_list = [("John", 25), ("Jane", 30)]
print_names_and_ages(name_age_list)


# 2. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

def create_dictionary():
    return {}

def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]


dictionary = create_dictionary()
print(dictionary)  # Empty dictionary

add_name_age(dictionary, "John", 25)
print(dictionary)  # {'John': 25}

update_age(dictionary, "John", 26)
print(dictionary)  # {'John': 26}

delete_name(dictionary, "John")
print(dictionary)  # {}


# 3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

def two_sum(nums, target):
    num_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

    return []


nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # [0, 1]


# 4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False

# Example usage
word = "madam"
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")


# 5. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # [11, 12, 22, 25, 64]


# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        word_count = len(content.split())

    return word_count

def write_word_count(filename, count):
    with open(filename, 'w') as file:
        file.write(f"Number of words: {count}")

# Example usage
input_filename = "input.txt"
output_filename = "output.txt"

word_count = count_words(input_filename)
write_word_count(output_filename, word_count)


# 10. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Example usage
num1 = 5
num2 = 0

division_result = divide_numbers(num1, num2)
print(division_result)  # Cannot divide by zero.
