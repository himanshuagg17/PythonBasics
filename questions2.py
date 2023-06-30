# Q1 Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


# Q2 ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

def display_numbers(numbers):
    for num in numbers:
        if num % 5 == 0:
            if num > 500:
                break
            if num > 150:
                continue
            print(num)

# Example usage
num_list = [12, 75, 150, 180, 145, 525, 50]
display_numbers(num_list)


# Q3 ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# ```
# s1 = "Ault"
# s2 = "Kelly"
# ```

# **Expected Output**:

def append_string(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]

    return s3

# Example usage
string1 = "Ault"
string2 = "Kelly"
result = append_string(string1, string2)
print("Result:", result)


# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

# **Given**:

# ```
# str1 = PyNaTive
# ```

# **Expected Output**:

def arrange_characters(string):
    sorted_string = sorted(string, key=lambda x: x.islower())

    return ''.join(sorted_string)


str1 = "PyNaTive"
result = arrange_characters(str1)
print("Result:", result)


# Q5 ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# **Given**:

# ```
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# ```

# **Expected output:**

def concatenate_lists(list1, list2):
    combined_list = [x + y for x, y in zip(list1, list2)] + list1[len(list2):] + list2[len(list1):]

    return combined_list


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = concatenate_lists(list1, list2)
print("Result:", result)


### Problem **6: Concatenate two lists in the following order**

# ```
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ```

# **Expected output:**

def concatenate_lists(list1, list2):
    combined_list = list1 + list2

    return combined_list


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = concatenate_lists(list1, list2)
print("Result:", result)


### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# **Given**

# ```
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# ```

# **Expected output:**


def iterate_lists(list1, list2):
    for item1, item2 in zip(list1, reversed(list2)):
        print(item1, item2)


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
iterate_lists(list1, list2)


### Problem **8: Initialize dictionary with default values**

# In Python, we can initialize the keys with the same values.

# **Given**:

# ```
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# ```

# **Expected output:**

def initialize_dictionary(keys, defaults):
    employee_dict = {key: defaults[key] for key in keys}

    return employee_dict

# Example usage
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = initialize_dictionary(employees, defaults)
print("Result:", result)



### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:

# ```
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# ```

# **Expected output:**

def extract_dictionary_keys(dictionary, keys):
    extracted_dict = {key: dictionary[key] for key in keys if key in dictionary}

    return extracted_dict

# Example usage
sample_dict = {
    "name": "Abraham",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
result = extract_dictionary_keys(sample_dict, keys)
print("Result:", result)


### Problem **10: Modify the tuple**

# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222

# **Given**:

# ```
# tuple1 = (11, [22, 33], 44, 55)
# ```

# **Expected output:**


def modify_tuple_element(tuple_data, new_value):
    # Convert the tuple to a list
    list_data = list(tuple_data)

    # Modify the desired element
    list_data[1][0] = new_value

    # Convert the list back to a tuple
    modified_tuple = tuple(list_data)

    return modified_tuple


tuple1 = (11, [22, 33], 44, 55)
new_value = 222
result = modify_tuple_element(tuple1, new_value)
print("Result:", result)
